from fastapi import APIRouter

user = APIRouter()


@user.get('/login')
def user_login():
    return {'user': '登录'}


@user.get('/reg')
def user_reg():
    return {"user": '注册'}
