def get_cats_info(path):
    """Зчитує дані про котів із файлу та повертає список словників"""

    result = []  # список для котів

    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()            # прибираємо перенос рядка
                cat_id, name, age = line.split(",")  # розбиваємо на id, ім'я, вік
                result.append({"id": cat_id, "name": name, "age": age})  # додаємо словник

        return result  # повертаємо список словників

    except FileNotFoundError:
        return []  # якщо файл не знайдено

    except ValueError:
        return []  # якщо формат рядка неправильний

if __name__ == "__main__":
    # виклик функції
    cats_info = get_cats_info("cats.txt")

    # вивід результату
    for cat in cats_info:
        print(cat)