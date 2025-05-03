import asyncio

"""
1. 协程快速上手
事件循环：就是把协程函数放入列表，遍历出当前可执行的函数来执行，直到所有函数都执行完成
"""


async def func():  # 定义了一个协程函数
    print("我是一个协程函数！")


# loop = asyncio.get_event_loop()  // 老写法
# loop.run_until_complete(func())
"""将协程函数加入到事件循环"""
asyncio.run(func())  # python 3.7 之后的新写法

"""
2. await 就是等待后续对象得到结果之后再继续向下走
await + 可等待对象 （即：协程对象、Future、Task对象 -> IO等待）
await 后面的东西执行完了才会往前走
"""


async def others():
    print("start")
    await asyncio.sleep(2)
    print('end')
    return '我是超级awit的返回值'


async def func2():
    print('执行协程函数内部代码')
    response = await others()
    print("IO请求结束，结果为：", response)


asyncio.run(func2())
