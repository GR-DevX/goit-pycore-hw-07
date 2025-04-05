from models import Record, AddressBook
import datetime

def hello():
    print("Ласкаво просимо до асистента-бота!")

def add_contact(book, name, phone):
    if not Record.validate_phone(phone):
        print("Телефонний номер має складатися з 10 цифр.")
        return

    for record in book.records:
        if record.name == name:
            record.phone = phone
            print(f"Номер телефону для {name} оновлено.")
            return
    book.add_record(Record(name, phone))
    print(f"Контакт {name} з номером {phone} додано.")

def change_phone(book, name, old_phone, new_phone):
    if not Record.validate_phone(new_phone):
        print("Телефонний номер має складатися з 10 цифр.")
        return

    for record in book.records:
        if record.name == name and record.phone == old_phone:
            record.phone = new_phone
            print(f"Телефон для {name} змінено.")
            return
    print("Невірна команда.")

def phone(book, name):
    for record in book.records:
        if record.name == name:
            print(f"Телефон для {name}: {record.phone}")
            return
    print("Контакт не знайдений.")

def show_all_contacts(book):
    if not book.records:
        print("Адресна книга порожня.")
    for record in book.records:
        print(record)

def add_birthday(book, name, birthday):
    for record in book.records:
        if record.name == name:
            record.birthday = birthday
            print(f"День народження для {name} додано.")
            return
    print("Контакт не знайдений.")

def show_birthday(book, name):
    for record in book.records:
        if record.name == name and record.birthday:
            print(f"День народження {name}: {record.birthday}")
            return
    print("Контакт не знайдений або день народження не вказано.")

def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        print("Список привітань на цьому тижні:")
        for item in upcoming_birthdays:
            print(f"Ім'я: {item['name']}, Дата привітання: {item['birthday']}")
    else:
        print("Немає днів народження в найближчий тиждень.")

def exit_program():
    print("Закриваю програму.")
    exit()
