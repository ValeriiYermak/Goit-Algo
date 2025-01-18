import networkx as nx
import matplotlib.pyplot as plt

# Створення графа (як у вас)
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

# Додавання станцій та шляхів до графа
for line, stops in stations.items():
    metro_graph.add_nodes_from(stops, line=line)
    edges = [(stops[i], stops[i + 1], distances[line][i]) for i in range(len(stops) - 1)]
    metro_graph.add_edges_from([(u, v, {"weight": w}) for u, v, w in edges], line=line)

# Алгоритм Дейкстри для знаходження найкоротших шляхів
def dijkstra_shortest_path(graph, source):
    lengths = nx.single_source_dijkstra_path_length(graph, source, weight='weight')
    return lengths

# Знайдемо найкоротші шляхи для кожної станції
shortest_paths = {}
for station in metro_graph.nodes():
    shortest_paths[station] = dijkstra_shortest_path(metro_graph, station)

# Візуалізація графа
pos = nx.spring_layout(metro_graph, seed=42)
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

# Висновки зберігаються у markdown форматі

# Визначимо максимальні ширини колонок
max_station_width = max(len(station) for station in shortest_paths.keys())
max_target_width = max(len(target) for paths in shortest_paths.values() for target in paths.keys())
max_length_width = max(len(f"{length:.6f}") for paths in shortest_paths.values() for length in paths.values())

# Визначимо ширину для кожної колонки
station_width = max(max_station_width, len("Найкоротші шляхи від станції"))
target_width = max(max_target_width, len("До станції"))
length_width = max(max_length_width, len("Відстань (км)"))

# Створимо шапку таблиці з динамічною шириною
markdown_report = f"""# Звіт про ефективність алгоритмів пошуку підрядків

| {'Найкоротші шляхи від станції': <{station_width}} | {'До станції': <{target_width}} | {'Відстань (км)': <{length_width}} |
|{'-' * (station_width + target_width + length_width + 6)}|
"""

# Виведемо найкоротші шляхи для кожної станції
for station, paths in shortest_paths.items():
    for target, length in paths.items():
        markdown_report += f"| {station: <{station_width}} | {target: <{target_width}} | {length: <{length_width}.6f} |\n"

# Записуємо звіт у файл
with open("report.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print("Звіт збережено у файл report.md.")
