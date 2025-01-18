import networkx as nx
import matplotlib.pyplot as plt

# Створення графа для Київського метрополітену
metro_graph = nx.Graph()

# Додамо станції та з'єднання між ними (спрощений приклад)
stations = {
    "Червона лінія": ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"],
    "Синя лінія": ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Льва Толстого", "Олімпійська", "Палац \"Україна\"", "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки"],
    "Зелена лінія": ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", "Кловська", "Печерська", "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний хутір"]
}

# Відстані між станціями (в умовних одиницях)
distances = {
    "Червона лінія": [1.5, 1.8, 2.0, 1.7, 1.4, 2.2, 1.9, 1.1, 0.9, 1.0, 1.6, 2.3, 2.5, 1.8, 1.2, 2.0, 2.1],
    "Синя лінія": [1.7, 1.5, 1.8, 2.0, 1.4, 1.2, 1.1, 0.8, 1.3, 1.6, 1.5, 1.7, 1.8, 2.2, 1.9, 2.1, 2.0],
    "Зелена лінія": [1.9, 1.6, 2.0, 1.3, 1.2, 1.4, 1.7, 2.5, 2.2, 1.8, 1.6, 1.7, 2.0, 2.3, 2.4]
}

# Додамо вершини та ребра до графа
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


# Аналіз основних характеристик
def analyze_network(metro_graph):
    print(f"Кількість станцій (вершин): {metro_graph.number_of_nodes()}")
    print(f"Кількість з'єднань (ребер): {metro_graph.number_of_edges()}")
    print("\nСтупені вершин:")
    for node in metro_graph.nodes():
        print(f"{node}: {metro_graph.degree(node)}")

    print("\nВідстані між сусідніми станціями:")
    for u, v, data in metro_graph.edges(data=True):
        print(f"{u} - {v}: {data['weight']} км")

    # Аналіз для найбільшої зв'язної компоненти
    if nx.is_connected(metro_graph):
        print(f"\nДіаметр мережі: {nx.diameter(metro_graph)}")
        print(f"Середня довжина найкоротшого шляху: {nx.average_shortest_path_length(metro_graph):.2f}")
    else:
        largest_cc = max(nx.connected_components(metro_graph), key=len)
        largest_subgraph = metro_graph.subgraph(largest_cc)
        print("\nМережа не є зв'язною.")
        print(f"Діаметр найбільшої зв'язної компоненти: {nx.diameter(largest_subgraph)}")
        print(
            f"Середня довжина найкоротшого шляху у найбільшій компоненті: {nx.average_shortest_path_length(largest_subgraph):.2f}")

    print(f"Щільність графа: {nx.density(metro_graph):.3f}")

analyze_network(metro_graph)