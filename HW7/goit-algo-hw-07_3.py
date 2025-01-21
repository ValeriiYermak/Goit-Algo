"""
Завдання 3

Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
"""
from graphviz import Digraph

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def calculate_sum(root):
    """
    Рекурсивно вираховуємо суму всіх значень в дереві.
    :param root:
    :return:
    """
    if not root:
        return 0
    return root.key + calculate_sum(root.left) + calculate_sum(root.right)


def visualize_tree(root):
    """
    Візуалізує дерево за допомогою Graphviz.

    :param root: Корінь дерева
    """

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
root.left = Node(6)
root.right = Node(25)
root.left.left = Node(2)
root.left.right = Node(9)
root.right.left = Node(18)
root.right.right = Node(30)

tree_sum = calculate_sum(root)
print(f"The sum of all values in the tree: {tree_sum}")

"Візуалізація Дерева"

tree_show = visualize_tree(root)
tree_show.render("Sum_tree", format="jpeg", cleanup=True)