from fastapi import FastAPI
import uvicorn
from typing import List
from pydantic import BaseModel, Field, field_validator
from datetime import date

myapp = FastAPI()
"""
使用pydantic来做请求体参数的类型、范围限制与检查
"""


class User(BaseModel):
    # name:str = Field(regex="^a") # 使用正则做限定
    age: int = Field(default=0, gt=0, lt=100)
    birth: date
    friends: List[int]

    """用装饰器validator来做 name 字段的校验规则"""
    @field_validator('name')
    @classmethod               # 定义为类方法，让pydantic可以在创建实例前直接调用该函数检验
    def name_must_alpha(cls, value: str) -> str: # cls是模型类本身，value即传入的值
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value


"""
1. 在这里的 User对象类型数据会自动进行 JSON序列化
2. 在这里的 int 类型限定，会使得自动将数字字符串给隐式转换为int,如果转换失再报错
"""


@myapp.post('/data')
async def data(user: User):
    print(user.dict)
    return user


if __name__ == '__main__':
    uvicorn.run("6_请求体参数:myapp", port=8080, reload=True)
