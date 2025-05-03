from fastapi import FastAPI
import uvicorn

myapp = FastAPI()

"""这里路径参数必须要和函数参数同名"""
@myapp.get("/user/{user_id}")
async def get_user(user_id):
    print("id:",user_id)
    return {'user_id': user_id}
"""
路径覆盖问题：  前面的会覆盖掉后面的， /user/1对应的逻辑永远不会是get_user2
"""
@myapp.get("/user/1")
async def get_user2():

    return {'user_id':"我是user 1" }





if __name__ == '__main__':

    uvicorn.run("4_路径参数:myapp", port=8080,reload=True)
