def filter_even_numbers():
    # Запрос ввода от пользователя
    user_input = input("Введите список чисел, разделенных пробелом: ")

    # Преобразуем строку в список целых чисел
    numbers = list(map(int, user_input.split()))

    # Фильтруем четные числа
    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Четные числа:", even_numbers)

# Запуск функции
filter_even_numbers()
