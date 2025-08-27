from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn, json
import os

app = FastAPI(title="Простой CRUD с JSON")

DATA_FILE = 'users.json'

@app.get("/")
def home():
    """Главная страница"""
    return {'Сообщение': "Простой CRUD API", "документация": "/docs"}


def save_users(users):
    """Сохраняет список пользователей в JSON файл"""
    with open(DATA_FILE, 'w', encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


@app.on_event("startup")
def startup():
    """Создает тестовых пользователей при первом запуске"""
    if not os.path.exists(DATA_FILE):
        test_users = [
            {"id": 1, "Имя": "Иван Петров", "возраст": 25 ,"email": "john@example.com"},
            {"id": 2, "Имя": "Петр Иванов", "возраст": 30 ,"email": "jane@example.com"},
            {"id": 3, "Имя": "Усейн болт", "возраст": 35 ,"email": "bob@example.com"}
        ]
        save_users(test_users)
        print("Тестовые пользователи созданы")


if __name__ == "__main__":
    uvicorn.run("task_api_json:app", host="127.0.0.1", port=8000, reload=True)