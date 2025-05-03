from fastapi import FastAPI
import uvicorn

myapp = FastAPI()


@myapp.get("/")
async def home():
    return {'user_id': 1001}


@myapp.get('/shop')
async def shop():
    return {'shop': '……'}


"""
命令行启动命令：  uvicorn 1_quickstart:myapp --reload
注意： . 会被解释成/  所以使用 _
"""
"""
直接使用代码启动 ：
"""
if __name__ == '__main__':
    """
    1.debug参数已经移除， reload参数即：开启热重载（修改的代码直接生效）
    2.接口文档： 127.0.0.1:8080/docs
    """

    uvicorn.run("1_quickstart:myapp", port=8080,reload=True)
