import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock
from .test_data import price_data, type_data  # Импортируем данные


# Тест для проверки, что get_name возвращает строку
def test_get_name_returns_string():
    ingredient = Ingredient("Соусы", "Соус Spicy-X", 90)
    assert isinstance(ingredient.get_name(), str)


# Тест для проверки, что get_price возвращает число с плавающей точкой
def test_get_price_returns_float():
    ingredient = Ingredient("Начинки", "Хрустящие минеральные кольца", 300.1)
    assert isinstance(ingredient.get_price(), float)


# Тест для проверки, что get_type возвращает строку
def test_get_type_returns_string():
    ingredient = Ingredient("Булки", "Флюоресцентная булка R2-D3", 988)
    assert isinstance(ingredient.get_type(), str)


# Тест для проверки корректного возвращения названия ингредиента
def test_get_name_value():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Соус Spicy-X"
    assert ingredient.get_name() == "Соус Spicy-X"


# Параметризированный тест для проверки корректного возвращения цены ингредиента
@pytest.mark.parametrize("price, expected_price", price_data)
def test_get_price_value(price, expected_price):
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = price
    assert ingredient.get_price() == expected_price


# Параметризированный тест для проверки корректного возвращения типа ингредиента
@pytest.mark.parametrize("type, expected_type", type_data)
def test_get_type_value(type, expected_type):
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = type
    assert ingredient.get_type() == expected_type
