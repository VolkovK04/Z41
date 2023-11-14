import random

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.size = 1
        self.left = None
        self.right = None

def size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = size(node.left) + size(node.right) + 1

def merge(left, right):
    if not left or not right:
        return left or right

    if left.priority > right.priority:
        left.right = merge(left.right, right)
        update_size(left)
        return left
    else:
        right.left = merge(left, right.left)
        update_size(right)
        return right

def split(root, index):
    if not root:
        return None, None

    if index <= size(root.left):
        left, right = split(root.left, index)
        root.left = right
        update_size(root)
        return left, root
    else:
        left, right = split(root.right, index - size(root.left) - 1)
        root.right = left
        update_size(root)
        return root, right

def insert(root, index, value):
    new_node = Node(value, random.randint(0, 10**9))
    left, right = split(root, index)
    return merge(merge(left, new_node), right)

def get_range_sum(root, from_index, to_index):
    _, left = split(root, from_index)
    left, _ = split(left, to_index - from_index + 1)
    return sum_tree(left)

def sum_tree(node):
    return node.value + sum_tree(node.left) + sum_tree(node.right) if node else 0

def run_tests():
    arr = [1, 3, 5, 7, 9, 11]
    root = None

    for i, value in enumerate(arr):
        root = insert(root, i, value)

    assert get_range_sum(root, 1, 4) == 24
    root = insert(root, 2, 6)
    assert get_range_sum(root, 1, 4) == 28
    assert get_range_sum(root, 0, 2) == 9
    root = insert(root, 0, 10)
    assert get_range_sum(root, 0, 2) == 18

    print("Все тесты успешно пройдены.")

run_tests()
