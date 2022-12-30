from fastapi import FastAPI
from routers import products, users

app = FastAPI()

#routers
app.include_router(products.router) #importo products en main
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola fast API!"

@app.get("/url")
async def url():
    return {"url":"https://github.com/mouredev/Hello-Python"}