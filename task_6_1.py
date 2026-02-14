def total_salary(path):
    total = 0   # загальна сума зарплат
    count = 0   # кількість працівників

    try:
        # відкриваємо файл для читання
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()              # видаляємо символ переносу рядка
                name, salary = line.split(",")  # розділяємо рядок на ім’я та зарплату

                total += int(salary)             # додаємо зарплату до загальної суми
                count += 1                      # збільшуємо лічильник

        # обчислюємо середню зарплату
        average = total // count if count > 0 else 0

        # повертаємо результат у вигляді кортежу (total, average)
        return total, average

    except FileNotFoundError:
        # якщо файл не знайдено
        return 0, 0

    except ValueError:
        # якщо файл має неправильний формат даних
        return 0, 0


# викликаємо функцію та зберігаємо результат
result = total_salary("Salary.txt")

# виводимо результат на екран
print(f"Загальна сума заробітної плати: {result[0]} \nСередня заробітна плата: {result[1]}")