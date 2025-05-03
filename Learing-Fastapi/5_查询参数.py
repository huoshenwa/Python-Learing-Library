from fastapi import FastAPI
import uvicorn
from typing import Union, Optional

myapp = FastAPI()

"""
声明不属于路径参数的其他函数参数时，他们将自动解释为“查询字符串”参数，
也就是url？之后用 & 分割的 key-value 键值对
"""


@myapp.get("/jobs/{kd}")
async def get_jobs(kd, xl=None, gj=None):  # 有默认参数即前端不用必须输入
    return {'kd': kd,
            'xl': xl,
            'gj': gj
            }

""""
Union[str, None] 即 类型限定为 str , None
Optional 即Union 的缩写， Optional[str] = Union[str, None]
"""
@myapp.get("/jobs2/{kd}")
async def get_jobs(kd,
                   xl: Union[None, str] = None,
                   gj: Optional[str] = None):  # 有默认参数即前端不用必须输入
    return {'kd': kd,
            'xl': xl,
            'gj': gj
            }


if __name__ == '__main__':
    uvicorn.run("5_查询参数:myapp", port=8080, reload=True)
