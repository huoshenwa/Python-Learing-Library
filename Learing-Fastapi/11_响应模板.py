import fastapi
from pydantic import BaseModel, EmailStr
import uvicorn
from typing import Union

myapp = fastapi.FastAPI()


# 就是通过类来定义客户端要发送的数据的模板 和 服务器要响应数据的模板
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@myapp.post('/user02', response_model=UserOut,
            response_model_exclude_unset=True,  # 返回客户端的数据排除空值数据
            response_model_include={'username'},  # 返回客户端的数据要包括模板的哪个字段
            response_model_exclude={'email'}  # 返回客户端的数据要排除模板的哪个字段
            )
def create_user(user: UserIn):
    return user


if __name__ == '__main__':
    uvicorn.run("11_响应模板:myapp", host='192.168.31.92', port=8080, reload=True)
