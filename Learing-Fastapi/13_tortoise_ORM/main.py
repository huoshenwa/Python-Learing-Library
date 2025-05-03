from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import uvicorn
from setting import TORTOISE_ORM
myapp = FastAPI()

# Tortoise ORM 配置
register_tortoise(
    app=myapp,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 是否自动创建表（生产环境建议关闭，用迁移工具）
    # add_exception_handlers=True,  # 是否添加 ORM 异常处理器（FastAPI 错误响应）
)

if __name__ == '__main__':
    uvicorn.run("main:myapp", host='192.168.31.92', port=8080, reload=True)