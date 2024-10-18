from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


# Тест для проверки установки булочки
def test_set_buns():
    burger = Burger()
    bun = Mock(spec=Bun)
    burger.set_buns(bun)
    assert burger.bun == bun


# Тест для проверки добавления ингредиента
def test_add_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient


# Тест для проверки удаления ингредиента
def test_remove_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


# Тест для проверки перемещения ингредиента
def test_move_ingredient():
    burger = Burger()
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == ingredient1


# Тест для проверки расчёта цены
def test_get_price():
    burger = Burger()
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 988
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 90
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 2066.0  # 988 * 2 (булочки) + 90 (ингредиент)


# Тест для проверки чека
def test_get_receipt():
    burger = Burger()
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Флюоресцентная булка R2-D3"
    bun.get_price.return_value = 988
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = "Соусы"
    ingredient.get_name.return_value = "Соус Spicy-X"
    ingredient.get_price.return_value = 90
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()

    # Проверка булочек
    assert "(==== Флюоресцентная булка R2-D3 ====)" in receipt
    # Проверка ингредиентов с категорией
    assert "= соусы Соус Spicy-X =" in receipt
    # Проверка общей стоимости
    assert "Price: 2066" in receipt
