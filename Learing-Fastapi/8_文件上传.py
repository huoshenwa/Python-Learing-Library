from fastapi import FastAPI, File, UploadFile
import uvicorn
from typing import List
import os

myapp = FastAPI()


# 只适合小文件、单文件上传
@myapp.post('/file')
async def get_file(file: bytes = File()):
    return {
        'file': len(file)
    }


# 多文件上传
@myapp.post('/files')
async def get_files(files: List[bytes] = File()):
    for i, file in enumerate(files):
        print(f'文件{i}长度为：{len(file)}')
    return {
        'file': f'上传了{len(files)}个文件'
    }


# 使用内置类型UploadFile，文件句柄的上传, 单文件
@myapp.post('/UploadFile')
async def get_file(file: UploadFile):
    print('file:', file.file)
    path = os.path.join('file', file.filename)
    os.makedirs('file',exist_ok=True)
    # print(file.file.read())
    with open(path, 'wb') as f:
        # 不推荐按行遍历来写入，1.二进制文件不存在按行，这样可能导致损坏 2.逐行读取小数据块并写入，效率比直接批量读写低
        # for line in file.file: 3. 这样些会造成文件丢失
        #     f.write(line)
        f.write(file.file.read())
    return {
        'file': f'上传的文件名字是：{file.filename}'
    }
# 使用内置类型UploadFile，文件句柄的上传, 多文件
@myapp.post('/uploadFiles')
async def getUploadFile(files:list[UploadFile]):
    os.makedirs('file', exist_ok=True)
    for file in files:
        path = os.path.join('file', file.filename)
        with open(path, 'wb') as f:
            f.write(file.file.read())
    return {
        'file': f'上传的文件名字是：{"、".join([file.filename for file in files])}'
    }


"""
file.file :
它是一个 存储在内存或磁盘中的临时文件（根据文件大小自动选择）。小文件会存在内存中，大文件会写入磁盘
你可以像操作普通文件对象一样操作它（比如 .read(), .write(), .seek() 等）。
当请求结束后，临时文件会自动清理（除非你显式保存它）
"""
# 下面是 推荐的大文件 内存友好 的写法：
# 文件大于 10M 就可以使用分块读取 ， 优先使用await 异步读取
@myapp.post('/uploadBigFiles')
async def get_Bigfiles(files:List[UploadFile]):
    os.makedirs('file', exist_ok=True)
    for file in files:
        path = os.path.join('file', file.filename)
        with open(path, 'wb') as f:
            while chunk := await file.read(1024 * 1024): # 每次读取 1MB
                f.write(chunk)
    return {
        'file': f'上传的文件名字是：{"、".join([file.filename for file in files])}'
    }
# 解答疑问  ：  为什么 使用 wb 而不是 ab
# 因为wb的覆盖是重新用 with open 打开文件后才会删除覆盖，而在with open 下面使用同一f写入文件用的是同一文件句柄，
# 文件写入一点内容，文件指针就会向后走，直到写完本次打开为止
if __name__ == '__main__':
    uvicorn.run("8_文件上传:myapp", port=8080, reload=True)
