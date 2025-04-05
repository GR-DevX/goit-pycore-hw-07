from commands import (
    hello, add_contact, change_phone, phone,
    show_all_contacts, add_birthday, show_birthday, birthdays, exit_program
)
from models import AddressBook

def main():
    book = AddressBook()
    hello()

    while True:
        command = input("Введіть команду: ").strip()

        if command.startswith("add "):
            parts = command.split()
            if len(parts) == 3:
                add_contact(book, parts[1], parts[2])

        elif command.startswith("change "):
            parts = command.split()
            if len(parts) == 4:
                change_phone(book, parts[1], parts[2], parts[3])

        elif command.startswith("phone "):
            parts = command.split()
            if len(parts) == 2:
                phone(book, parts[1])

        elif command == "all":
            show_all_contacts(book)

        elif command.startswith("add-birthday "):
            parts = command.split()
            if len(parts) == 3:
                add_birthday(book, parts[1], parts[2])

        elif command.startswith("show-birthday "):
            parts = command.split()
            if len(parts) == 2:
                show_birthday(book, parts[1])

        elif command == "birthdays":
            birthdays(book)

        elif command == "hello":
            hello()

        elif command == "exit" or command == "close":
            exit_program()

        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
