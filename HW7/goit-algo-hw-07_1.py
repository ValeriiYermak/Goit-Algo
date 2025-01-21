"""
Завдання 1

Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві.
"""
from graphviz import Digraph


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_in_bt(root):
    """
    Знаходить найбільше значення у двійковому дереві пошуку або AVL-дереві.

    :param root: Корінь дерева
    :return: Найбільше значення у дереві
    """
    if not root:
        raise ValueError("The tree is empty.")
    current = root
    while current.right:
        current = current.right
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
root = Node(12)
root.left = Node(10)
root.right = Node(32)
root.right.right = Node(41)
root.right.left = Node(30)

# Виклик функції
max_value = find_max_in_bt(root)
print(f"Найбільше значення у дереві: {max_value}")

"Візуалізація Дерева"

tree_show = show_tree(root)
tree_show.render("binary_max_tree", format="jpeg", cleanup=True)


