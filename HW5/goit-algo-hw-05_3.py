import timeit


def boyer_moore_search(text: str, pattern: str) -> int:
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    bad_char = {char: m for char in pattern}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i

    shifts = 0
    while shifts <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shifts + j]:
            j -= 1
        if j < 0:
            return shifts
        shifts += bad_char.get(text[shifts + m - 1], m)
    return -1


def knuth_morris_pratt_search(text: str, pattern: str) -> int:
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp_search(text: str, pattern: str, prime: int = 101) -> int:
    m, n = len(pattern), len(text)
    if m == 0:
        return -1

    base = 256
    hpattern = htext = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        hpattern = (hpattern * base + ord(pattern[i])) % prime
        htext = (htext * base + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i : i + m] == pattern:
                return i
        if i < n - m:
            htext = (htext * base - ord(text[i]) * h + ord(text[i + m])) % prime
            htext = (htext + prime) % prime

    return -1


# Завантаження текстів
with open("article1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("article2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

# Вибір підрядків для тестування
existing_substring = "алгоритм"
non_existing_substring = "неіснуючий підрядок"

# Функція для вимірювання часу


def measure_time(text: str, pattern: str, search_func, func_name: str):
    time_taken = timeit.timeit(lambda: search_func(text, pattern), number=1000)
    print(f"{func_name}: Пошук підрядка '{pattern}' зайняв {time_taken:.6f} секунд")
    return time_taken


results = {}

for text_name, text in zip(["article1.txt", "article2.txt"], [text1, text2]):
    if not text:
        continue
    print(f"\nТестування для {text_name}:")
    for substring in [existing_substring, non_existing_substring]:
        print(f"\nТест для підрядка: '{substring}'")
        bm_time = measure_time(text, substring, boyer_moore_search, "Boyer-Moore")
        kmp_time = measure_time(text, substring, knuth_morris_pratt_search, "KMP")
        rk_time = measure_time(text, substring, rabin_karp_search, "Rabin-Karp")

        results[(text_name, substring)] = {
            "Boyer-Moore": bm_time,
            "KMP": kmp_time,
            "Rabin-Karp": rk_time,
        }

# Визначення найшвидшого алгоритму
print("\nРезультати:")
for key, timings in results.items():
    fastest = min(timings, key=timings.get)
    print(f"Для {key}: найшвидший алгоритм - {fastest}")

# Висновки зберігаються у markdown форматі
markdown_report = """# Звіт про ефективність алгоритмів пошуку підрядків

|    Текст     |         Підрядок      | Boyer-Moore (с) | KMP (с)  | Rabin-Karp (с) | Найшвидший |
|--------------|-----------------------|-----------------|----------|----------------|------------|
"""

for (text_name, substring), timings in results.items():
    fastest = min(timings, key=timings.get)
    markdown_report += f"| {text_name: <10} | {substring: <21} | {timings['Boyer-Moore']: <15.6f} | {timings['KMP']: <8.6f} | {timings['Rabin-Karp']: <14.6f} | {fastest: <9} |\n"

with open("report.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)