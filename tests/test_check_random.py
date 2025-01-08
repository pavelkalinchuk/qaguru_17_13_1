import random
import allure


@allure.title("Пытаем удачу на чёт: 'чёт' - тест пройден, 'нечёт' - не пройден.")
def test_check_random():
    with allure.step("Генерируем рандомное число от 1 до 10"):
        random_integer = random.randint(1, 10)
    with allure.step("Проверяем сгенерированное число на чёт нечёт"):
        assert random_integer % 2 == 0, f"Проигрыш, выпал нечёт ({random_integer})"

