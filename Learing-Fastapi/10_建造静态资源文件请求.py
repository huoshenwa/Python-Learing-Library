import fastapi
from fastapi import Request
import uvicorn
from fastapi.staticfiles import StaticFiles
myapp = fastapi.FastAPI()

# 建造一个静态资源文件夹，给客户端通过url路径直接访问
# 第一个属性path 是客户端访问指定的静态文件夹所要使用的url路径
myapp.mount('/xxx',StaticFiles(directory='static'))

@myapp.post('/')
async def items(request: Request):
    return {
        "客户端url": request.url,
        '客户端IP地址': request.client.host,
        '客户端用户代理': request.headers.get('user-agent'),
        '客户端cookie': request.cookies
    }


if __name__ == '__main__':
    uvicorn.run("10_建造静态资源文件请求:myapp",host='192.168.31.92', port=8080, reload=True)
