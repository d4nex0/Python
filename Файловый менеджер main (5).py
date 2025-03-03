import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        return str(e)

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            return "Данные успешно записаны."
    except Exception as e:
        return str(e)

def delete_file(file_path):
    try:
        os.remove(file_path)
        return "Файл успешно удален."
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Чтение файла")
        print("2. Запись в файл")
        print("3. Удаление файла")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            file_path = input("Введите путь к файлу для чтения: ")
            content = read_file(file_path)
            print(f"Содержимое файла:\n{content}")

        elif choice == '2':
            file_path = input("Введите путь к файлу для записи: ")
            content = input("Введите содержимое для записи: ")
            result = write_file(file_path, content)
            print(result)

        elif choice == '3':
            file_path = input("Введите путь к файлу для удаления: ")
            result = delete_file(file_path)
            print(result)

        elif choice == '4':
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")
