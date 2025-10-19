from typing import Tuple, List, Dict, Callable, Any
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Неправильний формат. Використання: add [ім'я] [номер телефону]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return "Неправильний формат. Використання: change [ім'я] [новий номер телефону]"
    name, phone = args
    if name not in contacts:
        return f"Помилка: Контакт з ім'ям '{name}' не знайдено."
    contacts[name] = phone
    return "Contact updated."
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        return "Неправильний формат. Використання: phone [ім'я]"
    name = args[0]
    if name not in contacts:
        return f"Помилка: Контакт з ім'ям '{name}' не знайдено."
    return contacts[name]
def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "Наразі немає збережених контактів."
    result = "Усі контакти:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
def parse_input(user_input: str) -> Tuple[str, List[str]]:
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return "", []
def main():
    contacts: Dict[str, str] = {}
    commands: Dict[str, Callable[[List[str], Dict[str, str]], str]] = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": lambda args, c: show_all(c),
    }
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip()
            command, args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command in commands:
                handler = commands[command]
                print(handler(args, contacts))
            elif command == "":
                 continue
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"Помилка під час виконання команди: {e}. Спробуйте ще раз.")
if __name__ == "__main__":
    main()