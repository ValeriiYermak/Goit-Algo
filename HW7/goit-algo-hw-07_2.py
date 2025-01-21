"""
Завдання 2

Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві.
"""
from graphviz import Digraph


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_in_bt(root):
    """
    Знаходить найменше значення у двійковому дереві пошуку або AVL-дереві.

    :param root: Корінь дерева
    :return: Найменше значення у дереві
    """
    if not root:
        raise ValueError("The tree is empty.")
    current = root
    while current.left:
        current = current.left
    return current.key

def show_tree(root):
    def add_edges(graph, node):
        if node.left:
            graph.edge(str(node.key), str(node.left.key))
            add_edges(graph, node.left)
        if node.right:
            graph.edge(str(node.key), str(node.right.key))
            add_edges(graph, node.right)

    dot = Digraph()
    if root:
        dot.node(str(root.key))
        add_edges(dot, root)
    return dot


# Побудова дерева
root = Node(35)
root.left = Node(8)
root.right = Node(49)
root.right.right = Node(61)
root.right.left = Node(45)

# Виклик функції
max_value = find_min_in_bt(root)
print(f"Найменше значення у дереві: {max_value}")

"Візуалізація Дерева"

tree_show = show_tree(root)
tree_show.render("binary_min_tree", format="jpeg", cleanup=True)


