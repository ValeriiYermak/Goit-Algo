def binary_search_upper_bound(arr, target):
    """
    Виконує двійковий пошук для знаходження верхньої межі у відсортованому масиві.

    Параметри:
    arr (list): Відсортований масив дробових чисел
    target (float): Значення для пошуку

    Повертає:
    tuple: (кількість ітерацій, верхня межа)
    """
    left = 0
    right = len(arr) - 1
    iterations = 0

    # Якщо масив порожній або target більший за всі елементи
    if not arr or target > arr[-1]:
        return (0, None)

    # Якщо target менший за перший елемент
    if target <= arr[0]:
        return (1, arr[0])

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Знаходимо верхню межу
    upper_bound = arr[left] if left < len(arr) else None
    return (iterations, upper_bound)


# Тестові випадки
test_arrays = [
    ([1.0, 2.0, 3.0, 4.0, 5.0], 2.5),
    ([1.1, 2.2, 3.3, 4.4, 5.5], 3.3),
    ([0.5, 1.5, 2.5, 3.5], 4.0),
    ([0.1, 0.2, 0.3, 0.4], 0.0),
    ([], 1.0),
]

for arr, target in test_arrays:
    result = binary_search_upper_bound(arr, target)
    print(f"\nМасив: {arr}")
    print(f"Шукаємо: {target}")
    print(f"Результат: {result}")
    print(f"Кількість ітерацій: {result[0]}")
    print(f"Верхня межа: {result[1]}")
