from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


# Тест для проверки списка булочек
def test_available_buns():
    database = Database()
    buns = database.available_buns()

    assert isinstance(buns, list)  # Проверяем тип данных
    assert len(buns) == 3  # Проверяем, что есть 3 булочки
    assert all(isinstance(bun, Bun) for bun in buns)  # Проверяем, что все элементы — булочки


# Тест для проверки списка ингредиентов
def test_available_ingredients():
    database = Database()
    ingredients = database.available_ingredients()

    assert isinstance(ingredients, list)  # Проверяем тип данных
    assert len(ingredients) == 6  # Проверяем, что есть 6 ингредиентов
    assert all(
        isinstance(ingredient, Ingredient) for ingredient in ingredients)  # Проверяем, что все элементы — ингредиенты
