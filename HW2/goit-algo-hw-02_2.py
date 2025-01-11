from collections import deque

def is_palindrome(input_string):
    """
    Перевіряє, чи є рядок паліндромом.

    Параметри:
        input_string (str): Рядок для перевірки.

    Повертає:
        bool: True, якщо рядок є паліндромом, і False в іншому випадку.
    """
    # Фільтрація символів: видалення пробілів та переведення в нижній регістр
    filtered_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створення двосторонньої черги
    char_deque = deque(filtered_string)

    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Приклад використання
if __name__ == "__main__":
    test_string = f'({input("Введіть рядок: ")})'  # Приклад input: "A man, a plan, a canal, Panama"
    if is_palindrome(test_string):
        print(f"\"{test_string}\" є паліндромом.")
    else:
        print(f"\"{test_string}\" не є паліндромом.")

