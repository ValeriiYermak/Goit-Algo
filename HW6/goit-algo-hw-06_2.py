import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
metro_graph = nx.Graph()

stations = {
    "Червона лінія": ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська",
                      "Політехнічний інститут", "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна",
                      "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"],
    "Синя лінія": ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа",
                   "Поштова площа", "Майдан Незалежності", "Площа Льва Толстого", "Олімпійська", "Палац \"Україна\"",
                   "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки"],
    "Зелена лінія": ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", "Кловська", "Печерська",
                     "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця",
                     "Бориспільська", "Червоний хутір"]
}

distances = {
    "Червона лінія": [1.5, 1.8, 2.0, 1.7, 1.4, 2.2, 1.9, 1.1, 0.9, 1.0, 1.6, 2.3, 2.5, 1.8, 1.2, 2.0, 2.1],
    "Синя лінія": [1.7, 1.5, 1.8, 2.0, 1.4, 1.2, 1.1, 0.8, 1.3, 1.6, 1.5, 1.7, 1.8, 2.2, 1.9, 2.1, 2.0],
    "Зелена лінія": [1.9, 1.6, 2.0, 1.3, 1.2, 1.4, 1.7, 2.5, 2.2, 1.8, 1.6, 1.7, 2.0, 2.3, 2.4]
}

for line, stops in stations.items():
    metro_graph.add_nodes_from(stops, line=line)
    edges = [(stops[i], stops[i + 1], distances[line][i]) for i in range(len(stops) - 1)]
    metro_graph.add_edges_from([(u, v, {"weight": w}) for u, v, w in edges], line=line)

# Візуалізація графа
pos = nx.spring_layout(metro_graph, seed=42)  # Генеруємо позиції вершин
plt.figure(figsize=(10, 10))

nx.draw(
    metro_graph,
    pos,
    with_labels=True,
    node_size=500,
    node_color="skyblue",
    font_size=6,
    font_weight="bold",
    edge_color="gray"
)

# Додамо ваги ребер до графа
edge_labels = nx.get_edge_attributes(metro_graph, 'weight')
nx.draw_networkx_edge_labels(metro_graph, pos, edge_labels=edge_labels, font_size=5)

plt.title("Транспортна мережа Київського метрополітену", fontsize=16)
plt.show()


def dfs_path(graph, start, target):
    visited = set()
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == target:
                return path
            visited.add(vertex)
            for neighbor in set(graph[vertex]) - visited:
                stack.append((neighbor, path + [neighbor]))

    return None

def bfs_path(graph, start, target):
    visited = set()
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == target:
                return path
            visited.add(vertex)
            for neighbor in set(graph[vertex]) - visited:
                queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    # Порівняння DFS і BFS
    start, target = "Академмістечко", "Лісова"
    dfs_result = dfs_path(metro_graph, start, target)
    bfs_result = bfs_path(metro_graph, start, target)

    print("\nРезультати пошуку шляхів:")
    print(f"DFS шлях від {start} до {target}: {dfs_result}")
    print(f"BFS шлях від {start} до {target}: {bfs_result}")

    # Пояснення різниці
    print("\nПояснення:")
    print("DFS (глибина): рухається якомога глибше в одному напрямку, повертаючись тільки після досягнення глухого кута.")
    print("BFS (ширина): досліджує всі вершини на одному рівні перед переходом на наступний.")
