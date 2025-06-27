import random
from tree import *


def get_max(root):
    if root:
        current = root
        # Йдемо до самого низу дерева у правих гілках
        while current.right:
            current = current.right
        return current.key


def main():
    root = None
    keys = [random.randint(-100, 100) for _ in range(20)]

    for key in keys:
        root = insert(root, key)

    print()
    print(f"Згенеровані елементи дерева: {keys}")
    print(f"Наше дерево має вид: {root}")
    print(F"Найбільше значення в дереві: {get_max(root)}")
    visualisation(root)


if __name__ == "__main__":
    main()