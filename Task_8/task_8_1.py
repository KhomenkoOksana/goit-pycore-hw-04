def caching_fibonacci():
    """
    Створює функцію fibonacci(n) з кешуванням обчислених значень.
    """

    cache = {}  # словник для збереження вже обчислених чисел Фібоначчі

    def fibonacci(n):
        """
        Повертає n-те число Фібоначчі, використовуючи рекурсію та кеш.
        """

        # базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # якщо значення вже є в кеші — повертаємо його
        if n in cache:
            return cache[n]

        # рекурсивне обчислення з кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == '__main__':
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
