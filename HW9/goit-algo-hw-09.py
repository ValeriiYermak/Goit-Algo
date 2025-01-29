"""
Маємо набір монет [50, 25, 10, 5, 2, 1]. Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити
оптимальний спосіб видачі решти покупцеві.

Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, і
повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад, для суми
113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш
доступні номінали монет.
Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, але
використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї
суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим
способом. Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, базуючись на часі їх виконання або О
великому та звертаючи увагу на їхню продуктивність при великих сумах. Висвітліть, як вони справляються з великими сумами
та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях. Свої висновки додайте у файл readme.md
домашнього завдання.
"""

import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


# TEST:

amount = int(input("Enter the amount: "))
# Measure the time for drawing
start_time = time.time()
print("Greedy Algorithm Result:", find_coins_greedy(amount))
# Calculate and display time
finished_time = time.time() - start_time
print(f"Tame taken for calculating greedy algorithm: {finished_time:.16f} seconds")


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin
    return result


start_time1 = time.time()
print()
print("Dynamic Programming Algorithm Result:", find_min_coins(amount))
# Calculate and display time
finished_time1 = time.time() - start_time1
print(
    f"Tame taken for calculating dynamic programming algorithm: {finished_time1:.16f} seconds"
)
