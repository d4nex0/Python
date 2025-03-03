def recursive_max(numbers):
    # Базовый случай: если список состоит из одного элемента, вернуть этот элемент
    if len(numbers) == 1:
        return numbers[0]

    # Рекурсивный случай: найти максимум в подсписке и сравнить с текущим элементом
    max_of_rest = recursive_max(numbers[1:])
    return max(numbers[0], max_of_rest)

# Пример использования функции
def main():
    user_input = input("Введите список чисел, разделенных пробелом: ")
    numbers = list(map(int, user_input.split()))

    if numbers:  # Проверка на пустой список
        max_number = recursive_max(numbers)
        print("Максимальное число:", max_number)
    else:
        print("Список пуст.")

# Запуск программы
main()
