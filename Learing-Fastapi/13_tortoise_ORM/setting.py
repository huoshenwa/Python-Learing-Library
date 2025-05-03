TORTOISE_ORM = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",  # 使用 MySQL 引擎
                "credentials": {
                    "host": "127.0.0.1",      # 数据库主机地址
                    "port": 3306,             # 数据库端口（MySQL 默认 3306）
                    "user": "root",           # 数据库用户名
                    "password": "123456",    # 数据库密码
                    "database": "fastapi",    # 数据库名称
                    "charset": "utf8mb4",     # 字符编码（推荐 utf8mb4 支持完整 Unicode，如 emoji）
                    "connect_timeout": 30,    # 连接超时时间（秒）
                    "minsize": 1,             # 连接池最小连接数
                    "maxsize": 8,             # 连接池最大连接数
                }
            }
        },
        "apps": {
            "models": {
                "models": ["models",'aerich.models'],  # 指定包含模型的 Python 模块（通常是 models.py 或 models/ 目录）
                "default_connection": "default",  # 默认使用的连接（对应上面的 connections 配置）
            }
        },
        "use_tz": False,  # 是否使用时区（False 表示使用数据库本地时间）
        "timezone": "Asia/Shanghai",  # 时区设置（如果 use_tz=True 生效）
    }