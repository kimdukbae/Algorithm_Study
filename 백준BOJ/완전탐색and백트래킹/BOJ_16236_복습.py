class Node:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size


node1 = Node(0, 1, 10)
node2 = Node(1, 2, 5)
print(node1.x, node1.y, node1.size)
print(node2.x, node2.y, node2.size)
