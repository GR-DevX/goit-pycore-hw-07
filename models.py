import datetime

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        birthday_str = f" (День народження: {self.birthday})" if self.birthday else ""
        return f"{self.name}: {self.phone}{birthday_str}"

    @staticmethod
    def validate_phone(phone):
        """Функція для перевірки правильності номера телефону (10 цифр)."""
        if len(phone) == 10 and phone.isdigit():
            return True
        else:
            return False


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_upcoming_birthdays(self):
        today = datetime.date.today()  # Поточна дата
        week_from_today = today + datetime.timedelta(days=7)  # Дата через 7 днів
        upcoming_birthdays = []  # Список майбутніх днів народження

        for record in self.records:
            if record.birthday:  # Якщо є дата народження
                birthday_date = datetime.datetime.strptime(record.birthday, "%d.%m.%Y").date()

                # Якщо день народження вже був цього року, переносимо на наступний рік
                if birthday_date.replace(year=today.year) < today:
                    birthday_date = birthday_date.replace(year=today.year + 1)
                else:
                    birthday_date = birthday_date.replace(year=today.year)

                # Якщо день народження потрапляє в наступні 7 днів
                if today <= birthday_date <= week_from_today:
                    original_birthday = birthday_date.strftime("%d.%m.%Y")

                    # Якщо день народження припадає на вихідний
                    if birthday_date.weekday() == 5:  # Якщо субота
                        birthday_date += datetime.timedelta(days=2)  # Переносимо на понеділок
                        new_birthday = birthday_date.strftime("%d.%m.%Y")
                        print(f"День народження {record.name} припадає на суботу ({original_birthday}), привітання переносимо на понеділок: {new_birthday}")
                    elif birthday_date.weekday() == 6:  # Якщо неділя
                        birthday_date += datetime.timedelta(days=1)  # Переносимо на понеділок
                        new_birthday = birthday_date.strftime("%d.%m.%Y")
                        print(f"День народження {record.name} припадає на неділю ({original_birthday}), привітання переносимо на понеділок: {new_birthday}")

                    upcoming_birthdays.append({
                        "name": record.name,
                        "birthday": birthday_date.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays
