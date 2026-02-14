def parse_input(user_input):
    # розбиває введений рядок на команду та аргументи
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args, contacts):
    # додає новий контакт
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    # змінює номер існуючого контакту
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    # показує номер телефону за ім'ям
    if len(args) != 1:
        return "Invalid command."
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts):
    # показує всі контакти
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    # словник для збереження контактів
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        # отримуємо команду від користувача
        user_input = input(">>> ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command in ("exit", "close"):
            print("Good bye!")
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    # запуск програми
    main()
