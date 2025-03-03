import random
import string

def generate_random_password(length):
    if length < 1:
        return "Длина пароля должна быть больше нуля."

    # Определяем возможные символы для пароля
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Запрашиваем у пользователя длину пароля
length = int(input("Введите длину пароля: "))
random_password = generate_random_password(length)
print("Сгенерированный пароль:", random_password)
