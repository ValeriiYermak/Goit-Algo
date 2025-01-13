""""
Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний
алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений
емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні
оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів
використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з
цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі.
Зробіть висновки.
"""
import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i<len(left):
            arr[k]+left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr

# Generate datasets
sizes = [100, 1000, 5000]
results = {"Insertion Sort": {}, "Merge Sort": {}, "Timsort": {}}

for size in sizes:
    random_data = [random.randint(1,10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reversed_data= sorted_data[::-1]

    # Measure time for each algorithm
    results["Insertion Sort"][size] = {
        "random": timeit.timeit(lambda: insertion_sort(random_data.copy()), number=1),
        "sorted": timeit.timeit(lambda: insertion_sort(sorted_data.copy()), number=1),
        "reversed": timeit.timeit(lambda: insertion_sort(reversed_data.copy()), number=1),
    }

    results["Merge Sort"][size] = {
        "random": timeit.timeit(lambda: merge_sort(random_data.copy()), number=1),
        "sorted": timeit.timeit(lambda: merge_sort(sorted_data.copy()), number=1),
        "reversed": timeit.timeit(lambda: merge_sort(reversed_data.copy()), number=1),
    }

    results["Timsort"][size] = {
        "random": timeit.timeit(lambda: sorted(random_data), number=1),
        "sorted": timeit.timeit(lambda: sorted(sorted_data), number=1),
        "reversed": timeit.timeit(lambda: sorted(reversed_data), number=1),
    }

# Print results
for algo, data in results.items():
    print(f"\n{algo} Results:")
    for size, timings in data.items():
        print()
        print(f"Dataset size: {size}")
        for data_type, time_taken in timings.items():
            print(f"{data_type.capitalize()} data: {time_taken:.6f} seconds")

"""
Найкращий результат показав алгоритм сортування Timsort, який робить викликання вбудованих алгоритмів. Алгоритм
Timsort використовує вбудовані в Python алгоритми, а не кодує сам.
Заміри часу показали найшвидше сортування на масивах розміром 1000 і 5000 елементів.
"""