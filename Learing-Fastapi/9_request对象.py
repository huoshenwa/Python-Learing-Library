import fastapi
from fastapi import Request
import uvicorn
"""
request 对象  即是用来获取客户端信息的对象
"""
myapp  = fastapi.FastAPI()

@myapp.post('/items')
async def items(request:Request):
    return {
        "客户端url":request.url,
        '客户端IP地址':request.client.host,
        '客户端用户代理':request.headers.get('user-agent'),
        '客户端cookie':request.cookies
    }
if __name__ == '__main__':
    uvicorn.run("9_request对象:myapp", port=8080, reload=True)