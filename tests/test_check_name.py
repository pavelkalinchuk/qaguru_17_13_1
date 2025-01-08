import allure
import pytest


@pytest.mark.skip(reason="Тест в разработке")
@allure.title("Проверяем имя на корректность")
def test_check_name():
    assert True
