def check_delimiters(sequence):
    """
    Перевіряє симетричність розділювачів у рядку.

    Параметри:
        sequence (str): Рядок із символами-розділювачами.

    Повертає:
        str: Повідомлення про симетричність розділювачів.
    """
    stack = []
    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in sequence:
        if char in "({[":
            stack.append(char)  # Додати відкритий розділювач у стек
        elif char in ")}]":
            if not stack or stack[-1] != matching_pairs[char]:
                return f"{sequence}: Несиметрично"
            stack.pop()  # Видалити відповідний відкритий розділювач

    if stack:
        return f"{sequence}: Несиметрично"

    return f"{sequence}: Симетрично"

# Приклади використання
if __name__ == "__main__":
    test_sequences = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]

    for seq in test_sequences:
        print(check_delimiters(seq))

