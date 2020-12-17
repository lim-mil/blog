from peewee import CharField, IntegerField

from blog.models import BaseModel


class UserModel(BaseModel):
    username = CharField(max_length=64, index=True)
    password = CharField(max_length=128, index=True)


class Role(BaseModel):
    title = CharField(max_length=64, index=True, verbose_name='角色名称')


class Permisson(BaseModel):
     title = CharField(max_length=64, index=True, verbose_name='权限名称')
     url = CharField(max_length=512, index=True, verbose_name='含权限的URL')
     code = CharField(max_length=32, index=True, verbose_name='权限代码')
     group_id = IntegerField(index=True, verbose_name='所属权限组')
     menu_id = IntegerField(index=True, verbose_name='组内菜单')


class PermissionGroup(BaseModel):
    caption = CharField(max_length=64, index=True, verbose_name='权限组名称')
    menu_id = IntegerField(index=True)


class Menu(BaseModel):
    title = CharField(max_length=64)


class UsersRoles(BaseModel):
    user_id = IntegerField(index=True)
    role_id = IntegerField(index=True)


class RolesPermissions(BaseModel):
    role_id = IntegerField(index=True)
    permission_id = IntegerField(index=True)


class PermissionsGroups(BaseModel):
    permission_id = IntegerField(index=True)
    group_id = IntegerField(index=True)


class PermissionsMenus(BaseModel):
    permission_id = IntegerField()
    menu_id = IntegerField()
