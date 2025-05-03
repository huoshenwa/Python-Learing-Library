from fastapi import APIRouter

shop = APIRouter()


@shop.get('/food')
def shop_food():
    return {'shop': '食物'}


@shop.get('/bed')
def shop_bed():
    return {"shop": '床上用品'}
