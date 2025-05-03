import asyncio
import time

"""
与async def 相比 Task多了以下能力：
状态跟踪：查看是否完成、取消或报错（如 task.done()）。
结果获取：通过 task.result() 获取协程返回值（若完成）。
取消控制：可主动取消任务（task.cancel()）。
并发管理：多个 Task 可并行运行（如 asyncio.gather）。
"""
"""
1. Task是并发执行
下面的例子可知task对象与直接await的区别是： await就是单纯的等待，无法实现并发
"""


async def 倒水(n, h=None):
    if h:
        # time.sleep(1)  会阻塞整个线程 破坏并发
        await asyncio.sleep(1)
    print('开始倒水', n)


async def main():
    print("使用Task并发：")
    task1 = asyncio.create_task(倒水(2, 5))  # 创建任务1（开始执行）
    task2 = asyncio.create_task(倒水(1))  # 创建任务2（同时开始！）

    await task1  # 可选择性等待
    await task2  # 如果注释掉，main()可能提前结束


asyncio.run(main())
print("==============================")
"""
2. 比较标准的用法：  列表 + asyncio.wait
"""


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")
    task_list = {
        asyncio.create_task(func(), name="n1"),  # name即最后返回对象的标识名字
        asyncio.create_task(func(), name="n2")
    }

    print('main结束')
    done,pending = await asyncio.wait(task_list,timeout=0.4) # timeout 即设置最多等待时间
    print('done:',done)
    print('pending:',pending)
asyncio.run(main())
"""
done（已完成的任务集合）
包含所有 已经执行完毕 的 Task 对象（无论是正常完成还是抛出异常）。

你可以遍历 done 集合，获取每个任务的执行结果或异常信息。

pending（未完成的任务集合）
包含所有 仍在运行 的 Task 对象（可能是因为 timeout 时间到了，或者它们本身执行时间较长）。

你可以选择继续等待它们完成，或者手动取消它们（task.cancel()）
"""
"""
3.  task_list 可以写在外面
"""
task_list = [
    func(),
    func()
]
done,pending = asyncio.run(asyncio.wait(task_list))