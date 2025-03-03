def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Поиск среднего элемента
        L = arr[:mid]        # Левое подмножество
        R = arr[mid:]        # Правое подмножество

        merge_sort(L)        # Рекурсивная сортировка левой части
        merge_sort(R)        # Рекурсивная сортировка правой части

        i = j = k = 0

        # Слияние подмножеств
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Проверка, остались ли элементы в L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Проверка, остались ли элементы в R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Отсортированный массив:", arr)
