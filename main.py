from fastapi import FastAPI
from routes import user, todo, tag

app = FastAPI()

app.include_router(user.router)
app.include_router(todo.router)
app.include_router(tag.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
