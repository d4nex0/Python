def word_frequency(text):
    # Преобразуем текст в список слов, убирая знаки препинания
    words = text.lower().split()
    word_count = {}

    for word in words:
        # Убираем знаки препинания
        word = word.strip('.,!?"()[]{}<>:;"\'')
        if word:  # Проверяем, что слово не пустое
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

# Пример использования
if __name__ == "__main__":
    input_text = input("Введите текст: ")
    frequencies = word_frequency(input_text)
    for word, count in frequencies.items():
        print(f"{word}: {count}")
