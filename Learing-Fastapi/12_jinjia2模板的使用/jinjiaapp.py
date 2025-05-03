from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

myapp = FastAPI()
# 挂载静态文件
myapp.mount("/static", StaticFiles(directory="templates/static"), name="my_static")

templates = Jinja2Templates(directory='templates')

# 模板数据
template_data = {
    "store_name": "知识海洋书城",
    "book_count": 6,
    "current_year": 2023,
    "books": [
        # 保持之前的书籍数据不变
    ]
}

@myapp.get('/')
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",  # templates目录下要返回的 模板文件的文件名
        {
            "request":request,  # 为什么需要request对象：jinjia2存在模板上下文依赖，需要客户端的信息来解析
            **template_data
        },  # context 上下文对象，一个字典，用变量替换jinjia2模板里面占位符数据
    )


if __name__ == '__main__':
    uvicorn.run("jinjiaapp:myapp", host='192.168.31.92', port=8080, reload=True)
