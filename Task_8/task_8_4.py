def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
    return inner


def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


@input_error
def add_contact(args, contacts):
    name, phone = args  # може викликати ValueError
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]  # може викликати IndexError
    if name not in contacts:
        raise KeyError
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
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
    main()