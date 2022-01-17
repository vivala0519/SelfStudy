class Node:
    def __init__(self, item, next): # 생성될때 item, next를 받아야하고 어떤 특징이 있어야되냐면
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        topNode = self.top
        self.top = self.top.next

        return topNode.item

    def is_empty(self):
        return self.top is None