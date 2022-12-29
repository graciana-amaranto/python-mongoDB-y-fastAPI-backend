from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#inicia el server con el comando uvicorn users:app --reload

#puedo crear una identidad usando BaseModel
class User(BaseModel):
    id: int
    name: str
    rol: str
    age: int
    url: str

users_list = [User(id=1, name="Mercy", rol="support", age=30, url="https://overwatch.blizzard.com/es-es/"),
         User(id=2, name= "Ashe", rol="damage",age=32, url="https://overwatch.blizzard.com/es-es/"),
         User(id=3, name="Reinhardt", rol="tank", age=60, url="https://overwatch.blizzard.com/es-es/")]

#ejemplo no habitual pero posible:
@app.get("/usersjson")
async def usersjson():
    return [{"name": "Mercy", "rol": "support", "age": 30, "url": "https://overwatch.blizzard.com/es-es/"},
            {"name": "Ashe", "rol": "damage", "age": 32, "url": "https://overwatch.blizzard.com/es-es/"},
            {"name": "Reinhardt", "rol": "tank", "age": 60, "url": "https://overwatch.blizzard.com/es-es/"}]

#forma correcta: devuelve todos los usuarios
@app.get("/users")
async def users():
    return users_list
#basemodel me ayuda a transformar un objeto a json en lugar de hacerlo manualmente como en usersjason

#devuelve UN usuario por path
@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)

#devuelve un usuario por query   /userquery?id=1&name=Mercy
@app.get("/userquery/")
async def user(id:int):
    return search_user(id)


def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0] 
    except:
        return {"error": "No se ha encontrado el usuario"}