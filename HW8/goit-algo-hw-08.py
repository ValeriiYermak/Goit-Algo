"""
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи
з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній
сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

import heapq


def min_connection_cost(cables, maximize=False):
    # Sort the cables by length
    if maximize:
        cables = [-cable for cable in cables]
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Get the two shortest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Connect them

        cost = first + second
        total_cost += abs(cost)

        # Add the connected cable to the heap
        heapq.heappush(cables, cost if not maximize else -abs(cost))

    return total_cost


# Test
cable_lengths = [4, 5, 8, 12, 63, 91, 2]
min_cost = min_connection_cost(cable_lengths[:], maximize=False)
print(f"Minimal cost of connection is {min_cost}")

max_cost = min_connection_cost(cable_lengths[:], maximize=True)
print(f"Maximal cost of connection is {max_cost}")