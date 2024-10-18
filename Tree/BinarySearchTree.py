class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
