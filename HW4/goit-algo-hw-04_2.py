"""
Дано k відсортованих списків цілих чисел. Завдання — об'єднати їх у один відсортований список. При виконанні завдання
потрібно опиратися на алгоритм сортування злиттям. Реалізуй функцію merge_k_lists , яка приймає на вхід список
відсортованих списків та повертає відсортований список.
"""

from heapq import heappush, heappop


def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків у один відсортований список.

    :param lists: Список відсортованих списків
    :return: Відсортований список
    """
    min_heap = []  # Мінімальна купа для зберігання елементів
    for i, lst in enumerate(lists):
        if lst:  # Якщо список не порожній
            heappush(min_heap, (lst[0], i, 0))  # Додаємо перший елемент, індекс списку та позицію у списку

    result = []
    while min_heap:
        val, list_idx, elem_idx = heappop(min_heap)  # Витягуємо мінімальний елемент
        result.append(val)  # Додаємо його до результату

        # Якщо у списку ще є елементи, додаємо наступний до купи
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return result


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
