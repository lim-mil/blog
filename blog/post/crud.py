from typing import Optional

from blog.post.models import PostModel, PostCategoryModel
from blog.post.schemas import PostIn, PostCategory, PostCategoryIn, PostOut, PostCategoryOut, PostOutList, PostUpdate, \
    PostOutListItem, CategoryPostOut


def create_post(post: PostIn):
    PostModel.create(**post.dict())


def retrive_post_by_id(id: int):
    post_model: Optional[PostModel] = PostModel.get_by_id(id)
    post = PostOut.from_orm(post_model)
    post.category = PostCategoryOut.from_orm(PostCategoryModel.get_by_id(post_model.category_id))
    return post


def update_post_by_id(id: int, post: PostUpdate):
    PostModel.update(**post.dict(exclude_unset=True)).where(PostModel.id == id).execute()


def delete_post_by_id(id: int):
    PostModel.delete_by_id(id)


def create_post_category(category: PostCategoryIn):
    PostCategoryModel.create(**category.dict())


def retrive_post_category_by_id(id: int):
    category = PostCategoryModel.get_by_id(id)
    return category


def update_post_category_by_id(id:int, category: PostCategory):
    PostCategoryModel.update(**category.dict()).where(PostCategoryModel.id == id).execute()


def delete_post_category_by_id(id: int):
    PostCategoryModel.delete_by_id(id)


def list_post(page: Optional[int], step: Optional[int]):
    if page and step:
        post_list_model = PostModel.select().limit(page).offset((page-1) * step)
    else:
        post_list_model = PostModel.select()
    result = PostOutList()
    for post_model in post_list_model:
        post = PostOutListItem.from_orm(post_model)
        post.category = PostCategoryOut.from_orm(PostCategoryModel.get_by_id(post_model.category_id))
        result.post_list.append(post)
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
        category: PostCategoryOut = PostCategoryOut.from_orm(category_model)
        category.posts = []
        for post_id in category_model.posts_set:
            post_model = PostModel.get_by_id(post_id)
            post = CategoryPostOut.from_orm(post_model)
            category.posts.append(post)
        result.append(PostCategoryOut.from_orm(category))
    return result


def update_post_category(id: int, category: PostCategory):
    PostCategoryModel.update(category.dict(exclude_none=True)).where(PostCategoryModel.id == id).execute()


if __name__ == '__main__':
    PostModel.update(title='ttt').where(PostModel.id==1)
