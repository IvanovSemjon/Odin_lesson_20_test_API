from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, json
import os

app = FastAPI(title="Простой CRUD с JSON")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = 'users.json'


def load_users():
    return json.load(open(DATA_FILE, 'r', encoding="utf-8"))


@app.get("/")
def home():
    """Главная страница"""
    return FileResponse('index_2.html')


@app.get("/users")
def get_users():
    """Возвращает список пользователей из JSON файла"""
    return load_users()


@app.get("/users/stats")
def get_stats():
    """Возвращает статистику по пользователям"""
    users = load_users()
    ages = [user['возраст'] for user in users]
    youngest = min(users, key=lambda x: x['возраст'])
    oldest = max(users, key=lambda x: x['возраст'])
    return {
        'total_users': len(users),
        'avg_age': sum(ages) / len(ages),
        'youngest': youngest,
        'oldest': oldest
    }

@app.get("/users/search/{name}")
def get_user_by_name(name: str):
    """Возвращает информацию о пользователе по его имени"""
    users = load_users()
    print(1, name)
    for user in users:
        if name.lower() in user['Имя'].lower():
            return user
    return {'error': 'Пользователь не найден'}
    

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Возвращает информацию о пользователе по его ID"""
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            return user
    return {'error': 'Пользователь не найден'}


@app.post("/users")
def create_user(user: dict):
    """Создает нового пользователя"""
    users = load_users()
    for u in users:
        if u['email'] == user['email']:
            return {'error': 'Пользователь с таким email уже существует'}
    user['id'] = len(users) + 1
    users.append(user)
    save_users(users)
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    """Обновляет информацию о пользователе по его ID"""
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            user.update(updated_user)
            save_users(users)
            return user
    return {'error': 'Пользователь не найден'}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Удаляет пользователя по его ID"""
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            save_users(users)
            return {'message': 'Пользователь удален'}
    return {'error': 'Пользователь не найден'}



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