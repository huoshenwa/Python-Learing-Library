from fastapi import FastAPI
import uvicorn

myapp = FastAPI()


@myapp.post("/", tags=["这是home测试接口tags"],
            summary="this is home 测试 summary",
            description='这是home测试的 description',
            response_description="这是home接口的响应描述")
async def home():
    return {'user_id': 1001}


@myapp.post("/item", tags=["这是item测试接口tags"],
            summary="this is home 测试 summary",
            description='这是home测试的 description',
            response_description="这是home接口的响应描述",
            deprecated=True,) # 废弃接口
async def item():
    return {'item': 1001}


if __name__ == '__main__':
    uvicorn.run("2_路径操作装饰器参数:myapp", port=8080, reload=True)
