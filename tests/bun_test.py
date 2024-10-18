from praktikum.bun import Bun


# Тест для проверки, что get_name возвращает строку
def test_get_name_returns_string():
    bun = Bun("Флюоресцентная булка R2-D3", 988)
    assert isinstance(bun.get_name(), str)


# Тест для проверки, что get_price возвращает число с плавающей точкой
def test_get_price_returns_float():
    bun = Bun("Краторная булка N-200i", 1.1)
    assert isinstance(bun.get_price(), float)


# Тест для проверки корректного возвращения названия булочки
def test_get_name_value():
    bun = Bun("Флюоресцентная булка R2-D3", 988)
    assert bun.get_name() == "Флюоресцентная булка R2-D3"


# Тест для проверки корректного возвращения цены булочки
def test_get_price_value():
    bun = Bun("Краторная булка N-200i", 1255)
    assert bun.get_price() == 1255.0
