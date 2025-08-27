from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"Ты ввел": item_id, "q": q}


@app.get('/add/{a}/{b}')
def add(a: float, b: float):
    return (f'{a} + {b} = {a + b}')


@app.get('/subtract/{a}/{b}')
def subtract(a: float, b: float):
    return (f'{a} - {b} = {a - b}')


@app.get('/multiply/{a}/{b}')
def multiply(a: float, b: float):
    return (f'{a} * {b} = {a * b}')


@app.get('/divide/{a}/{b}')
def divide(a: float, b: float):
    if b == 0:
        return ('На ноль делить нельзя')
    return (f'{a} / {b} = {a / b}')


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)