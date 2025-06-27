import random
from tree import *


def get_sum(root):
    if not root:
        return 0
    # рекурсивно обходимо значення всіх ключів вершин та додаємо до нього значення дочірніх
    return root.key + get_sum(root.left) + get_sum(root.right)


def main():
    root = None
    keys = [random.randint(-100, 100) for _ in range(20)]
    keys = [10, 20, 30, 25, 28, 27, -1, 15, 5, 3, 8, 12, 18, 22, 35, 40, 50, 45, 60, 70, 65, 55, 75]

    for key in keys:
        root = insert(root, key)

    print(get_sum(root))
    print(f"Згенеровані елементи дерева: {keys}")
    print(f"Наше дерево має вид: {root}")
    print(f"Сума всіх значень в дереві: {get_sum(root)}")
    visualisation(root)


if __name__ == "__main__":
    main()