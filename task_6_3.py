import sys
from pathlib import Path
from colorama import init, Fore

# ініціалізація colorama
init(autoreset=True)


def print_dir_structure(path: Path, prefix: str = "") -> None:
    """Рекурсивно виводить структуру директорії"""

    for item in path.iterdir():
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}📁 {item.name}")
            print_dir_structure(item, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN}📄 {item.name}")


def main() -> None:
    # перевірка аргументів командного рядка
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: не вказано шлях до директорії")
        return

    dir_path = Path(sys.argv[1])

    # перевірка існування шляху
    if not dir_path.exists():
        print(Fore.RED + f"Помилка: шлях '{dir_path}' не існує")
        return

    # перевірка що це директорія
    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: шлях '{dir_path}' не є директорією")
        return

    print(Fore.YELLOW + f"\nСтруктура директорії: {dir_path}\n")

    print_dir_structure(dir_path)


if __name__ == "__main__":
    main()
