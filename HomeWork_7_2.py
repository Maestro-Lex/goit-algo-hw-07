import random
from tree import *


def get_min(root):
    if root:
        current = root
        # Йдемо до самого низу дерева у лівих гілках
        while current.left:
            current = current.left
        return current.key


def main():
    root = None
    keys = [random.randint(-100, 100) for _ in range(20)]

    for key in keys:
        root = insert(root, key)

    print()
    print(f"Згенеровані елементи дерева: {keys}")
    print(f"Наше дерево має вид: {root}")
    print(f"Найменше значення в дереві: {get_min(root)}")
    visualisation(root)


if __name__ == "__main__":
    main()