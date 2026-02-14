from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)


def print_dir_structure(path: Path, prefix=""):
    """Рекурсивний вивід структури директорії з кольорами та іконками"""
    for item in path.iterdir():
        if item.is_dir():
            # Директорія синім кольором з іконкою 📁
            print(f"{prefix}{Fore.BLUE}📁 {item.name}")
            print_dir_structure(item, prefix + "    ")  # рекурсія для піддиректорій
        else:
            # Файл зеленим кольором з іконкою 📄
            print(f"{prefix}{Fore.GREEN}📄 {item.name}")


def main():
    # Запит шляху у користувача
    user_input = input("Введіть шлях до директорії: ").strip()
    dir_path = Path(user_input)

    # Перевірка існування та типу
    if not dir_path.exists():
        print(Fore.RED + f"Помилка: шлях '{dir_path}' не існує")
        return
    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: шлях '{dir_path}' не є директорією")
        return

    # Заголовок
    print(Fore.YELLOW + f"\nСтруктура директорії: {dir_path}\n")

    # Вивід структури
    print_dir_structure(dir_path)


if __name__ == "__main__":
    main()
