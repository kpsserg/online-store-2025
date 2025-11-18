# src/main.py
from fastapi import FastAPI

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# Именно эта строчка создаёт переменную "app"!
app = FastAPI(
    title="Мой интернет-магазин Сергея",
    description="Учусь у лучшего учителя в мире ❤️",
    version="0.1.0"
)
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

@app.get("/")
def read_root():
    return {"message": "Привет! Сервер работает!"}


@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Привет, {name}! Скоро здесь будет магазин =)"}


# Добавь это для домашки (список товаров)
fake_products = [
    {"id": 1, "name": "iPhone 15", "price": 109990, "in_stock": True},
    {"id": 2, "name": "AirPods Pro 2", "price": 23990, "in_stock": True},
    {"id": 3, "name": "Чехол MagSafe", "price": 4990, "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": fake_products}

# TheEnd4