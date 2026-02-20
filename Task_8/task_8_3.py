import sys


def parse_log_line(line: str) -> dict:
    """
    Парсить один рядок логу та повертає словник з компонентами:
    дата, час, рівень логування та повідомлення.
    """
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return {}

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> list:
    """
    Завантажує лог-файл та повертає список словників з розібраними логами.
    """
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        sys.exit(1)
    except IOError:
        print("Помилка читання файлу.")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує логи за вказаним рівнем логування.
    """
    level = level.upper()
    return [log for log in logs if log.get("level") == level]


def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts = {}

    for log in logs:
        level = log.get("level")
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts


def display_log_counts(counts: dict):
    """
    Виводить результати у вигляді таблиці.
    """
    print("\nРівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    """
    Головна функція програми. Обробляє аргументи командного рядка.
    """
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)

        print(f"\nЗаписи рівня {level_filter.upper()}:")
        print("-" * 40)

        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")


if __name__ == "__main__":
    main()