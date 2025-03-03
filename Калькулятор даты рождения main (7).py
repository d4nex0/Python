from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Запрашиваем у пользователя дату рождения
birthdate_input = input("Введите дату рождения (в формате ГГГГ-ММ-ДД): ")
birthdate = datetime.strptime(birthdate_input, '%Y-%m-%d')

age = calculate_age(birthdate)
print("Ваш возраст:", age)
