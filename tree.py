import matplotlib.pyplot as plt
import networkx as nx


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def visualisation(root):
    G = nx.DiGraph()

    def add_edges(node, pos, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.key)
            if node.left:
                G.add_edge(node.key, node.left.key)
                l = x - 1 / 2 ** layer
                pos[node.left.key] = (l, y - 1)
                add_edges(node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                G.add_edge(node.key, node.right.key)
                r = x + 1 / 2 ** layer
                pos[node.right.key] = (r, y - 1)
                add_edges(node.right, pos, x=r, y=y - 1, layer=layer + 1)

    pos = {root.key: (0, 0)}
    add_edges(root, pos)

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold')
    plt.title("AVL Tree Visualization")
    plt.show()


if __name__ == "__main__":
    # Driver program to test the above functions
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)
        print("AVL-Дерево:")
        print(root)

    # Delete
    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = delete_node(root, key)
        print("Видалено:", key)
        print("AVL-Дерево:")
        print(root)

    visualisation(root)