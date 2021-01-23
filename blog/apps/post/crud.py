from typing import Optional, List

from blog.apps.post.models import PostModel, PostCategoryModel
from blog.apps.post.schemas import PostInCreate, PostInResponse, PostCategoryInPost, PostInUpdate, \
    BasePostCategory, PostInListResponse, PostCategoryInResponse, PostInPostCategory, PostCategorySimpleInResponse


def create_post(post: PostInCreate):
    PostModel.create(**post.dict())


def retrive_post_by_id(id: int):
    post_model: Optional[PostModel] = PostModel.get_by_id(id)
    post = PostInResponse.from_orm(post_model)
    post.category = PostCategoryInPost.from_orm(PostCategoryModel.get_by_id(post_model.category_id))
    return post


def update_post_by_id(id: int, post: PostInUpdate):
    PostModel.update(**post.dict(exclude_unset=True)).where(PostModel.id == id).execute()


def delete_post_by_id(id: int):
    PostModel.delete_by_id(id)


def create_post_category(category: BasePostCategory):
    PostCategoryModel.create(**category.dict())


def retrive_post_category_by_id(id: int):
    category = PostCategoryModel.get_by_id(id)
    return category


def update_post_category_by_id(id:int, category: BasePostCategory):
    PostCategoryModel.update(**category.dict()).where(PostCategoryModel.id == id).execute()


def delete_post_category_by_id(id: int):
    PostCategoryModel.delete_by_id(id)


def list_post(page: Optional[int], step: Optional[int]):
    if page and step:
        post_list_model = PostModel.select().limit(step).offset((page-1) * step)
    else:
        post_list_model = PostModel.select()
    result: List[PostInResponse] = []
    for post_model in post_list_model:
        post = PostInListResponse.from_orm(post_model)
        post.category = PostCategoryInPost.from_orm(PostCategoryModel.get_by_id(post_model.category_id))
        result.append(post)
    return result


def list_post_category():
    """
    所有文章分类
    :return:
    """
    category_models = PostCategoryModel.select()
    result = []
    for category_model in category_models:
        category_model: PostCategoryModel
        category: PostCategoryInResponse = PostCategoryInResponse.from_orm(category_model)
        category.posts = []
        for post_id in category_model.posts_set:
            post_model = PostModel.get_by_id(post_id)
            post = PostInPostCategory.from_orm(post_model)
            category.posts.append(post)
        result.append(PostCategoryInResponse.from_orm(category))
    return result


def update_post_category(id: int, category: BasePostCategory):
    PostCategoryModel.update(category.dict(exclude_none=True)).where(PostCategoryModel.id == id).execute()


def list_post_category_simple():
    result = []
    categories = PostCategoryModel.select()
    for category in categories:
        result.append(PostCategorySimpleInResponse.from_orm(category))
    return result


if __name__ == '__main__':
    PostModel.update(title='ttt').where(PostModel.id==1)
