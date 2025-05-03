from fastapi import FastAPI, Form
import uvicorn

myapp = FastAPI()


@myapp.post('/regin')
async def reg(username: str = Form(), password: str = Form()):
    return {
        'username': username,
        'password': password
    }


if __name__ == '__main__':
    uvicorn.run("7_form表单数据:myapp", port=8080, reload=True)
