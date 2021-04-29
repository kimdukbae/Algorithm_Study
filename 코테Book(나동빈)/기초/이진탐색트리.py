class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # 이진 탐색 트리에 노드 삽입
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # 이진 탐색 트리에서 찾고자하는 값 탐색
    def search(self, want_word):
        if want_word < self.data:
            if self.left is None:
                return str(want_word) + " Not Found"
            return self.left.search(want_word)
        elif want_word > self.data:
            if self.right is None:
                return str(want_word) + " Not Found"
            return self.right.search(want_word)
        else:
            print(str(self.data) + ' is Found')

    # 이진 탐색 트리 출력
    def print_Tree(self):
        if self.left:
            self.left.print_Tree()
        print(self.data)
        if self.right:
            self.right.print_Tree()


root = Node(10)
root.insert(9)
root.insert(8)
root.insert(7)
print(root.search(7))
print(root.search(21))
