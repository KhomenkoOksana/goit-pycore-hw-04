import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, який знаходить та повертає всі дійсні числа з тексту.
    Числа в тексті відокремлені пробілами.
    """
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r"\b\d+\.?\d*\b"

    # Знаходимо всі числа у тексті
    matches = re.findall(pattern, text)

    # Повертаємо кожне знайдене число як float
    for number in matches:
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    """
    Обчислює загальну суму чисел, використовуючи генератор generator_numbers.
    """
    total = 0.0

    # Проходимося по генератору та додаємо кожне число до суми
    for value in func(text):
        total += value

    return total


if __name__ == "__main__":
    text = "Income for January is 800.35 and for February is 2000.08 and bonus 500"

    result = sum_profit(text, generator_numbers)
    print(f"Загальний прибуток: {result}")