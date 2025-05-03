- pip install fastapi  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- 服务器：
- pip install uvicorn  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- 表单提交相关：
- pip install python-multipart  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- 数据验证：
- pip install pydantic  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- tortoise ORM  数据库对象关系映射：
- pip install tortoise-orm  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com 
#### asyncmy. 安装 MySQL 异步驱动（任选其一）
- ##### 方案1：安装 asyncmy（推荐，性能更好）
- pip install asyncmy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- ##### 方案2：安装 aiomysql（兼容性更好）
- pip install aiomysql -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

- ####  Aerich 是 Tortoise ORM 的数据库迁移工具，需要单独安装：
- pip install aerich  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
- Aerich 还需要以下任意一个 TOML 处理库来生成配置文件：
-pip install tomli_w (Python 3.7+ 推荐) 
-pip install tomlkit (功能更全)
