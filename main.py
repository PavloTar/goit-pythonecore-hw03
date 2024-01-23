# ЗАВДАННЯ 1

# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime, timedelta
import random
import re

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        date_difference = input_date - current_date
        return date_difference.days
    
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

# Приклад використання
print("\n================================ ЗАВДАННЯ 1 ======================================\n")
today = datetime.today().strftime('%Y-%m-%d')  # Поточна дата у форматі 'РРРР-ММ-ДД'
test_date = "2024-10-09"
result = get_days_from_today(test_date)
print(f"Сьогодні {today}, до  дати {test_date} різниця у днях: {result}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# ЗАВДАННЯ 2

# необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

def get_numbers_ticket(min, max, quantity):
    if 1 <= min <= 1000 and 1 <= max <= 1000 and min <= quantity <= max:
        numbers = random.sample(range(min, max+1), quantity)
        return sorted(numbers)
    else:
        return []

# Приклад використання
print("\n================================ ЗАВДАННЯ 2 ======================================\n")

min = 1
max = 49
quantity = 6
print(f"Вхідні дані: min = {min}, max= {max}, кількість випадкових чисел - {quantity} ")
result = get_numbers_ticket(min, max, quantity)
print(result)

#------------------------------------------------------------------------------------------------------------------------------------------------------------


# ЗАВДАННЯ 3

# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку.
# Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'.
# Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r"[^0-9+]", "", phone_number)
    
    if not cleaned_number.startswith("+") and len(cleaned_number) == 10 :   # якщо номер не починається з + і не має міжнародного коду а лише сам номер телефону (для України довжина  = 10 цифр)
        # Додаємо міжнародний код для України '+38'
        cleaned_number = "+38" + cleaned_number
    elif not cleaned_number.startswith("+") and cleaned_number.startswith("38"): # якщо номер має міжнародний код але немає "+"" на початку
        cleaned_number = "+" + cleaned_number

    return cleaned_number


# Приклад використання

print("\n================================ ЗАВДАННЯ 3 ======================================\n")
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(f"Вхідні дані: {raw_numbers}")
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# ЗАВДАННЯ 4

# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays,
# яка допоможе вам визначати, кого з колег потрібно привітати.

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        #Конвертуємо рядок дня народження користувача у об'єкт дати
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        #Визначаємо день народження у поточному році.
        birthday_this_year = birthday.replace(year=today.year)

        #: Перевіряємо, чи день народження вже відбувся в цьому році
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) #Якщо так, визначаємо день народження у наступному році.

        #Визначаємо кількість днів до наступного дня народження.
        days_until_birthday = (birthday_this_year - today).days

        #Перевіряємо, чи дні до наступного дня народження менше або рівні 7.
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() in [5, 6]:  #Перевіряємо, чи день народження припадає на суботу або неділю.
                days_until_birthday += (7 - birthday_this_year.weekday()) # Якщо так, переносимо дату привітання на наступний понеділок.

            congratulation_date = today + timedelta(days=days_until_birthday) # Визначаємо дату привітання
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d") # Форматуємо дату привітання у вказаний формат рядка.

            #додаємо об'єкт в список для виводу іменинників та днів їх привітань
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

# Приклад використання

print("\n================================ ЗАВДАННЯ 4 ======================================\n")
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
    {"name": "Bob Doe", "birthday": "1984.01.20"},
    {"name": "Liza Smith", "birthday": "1984.02.22"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(f"Вхідні дані: {users}")
print("Список привітань на цьому тижні:", upcoming_birthdays)