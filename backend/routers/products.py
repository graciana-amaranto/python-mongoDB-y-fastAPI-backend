from fastapi import APIRouter

router = APIRouter(prefix="/products", #agrega /products autom. a cada path
                responses={404: {"message":"no encontrado"}},  #msj de error por defecto
                tags=["products"]) 

products_list = ["producto 1", "producto 2", "producto 3", "producto 4"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")  #/products/{id}
async def products(id:int):
    return products_list[id]


