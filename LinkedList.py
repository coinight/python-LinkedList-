class Node:
    def __init__(self, value=None, Nnext=None):
        self.value = value
        self.next = Nnext


class LinkedList:
    def __init__(self) -> None:
        self.header: Node = None

    def __getitem__(self, item):
        temp = self.header
        i = 0
        while i < item:
            if temp.next is None:
                raise ValueError('index error')
            temp = temp.next
            i += 1
        return temp

    def __delitem__(self, key):
        if key == 0:
            self.header = self.header.next
            return
        temp = self.__getitem__(key - 1)
        temp.next = temp.next.next

    def append(self, index, node: Node):
        if not issubclass(type(node), Node):
            raise ValueError('Not a Node')
        if index == 0:
            node.next = self.header.next
            self.header = node
        temp = self.__getitem__(index - 1)
        node.next = temp.next
        temp.next = node

    def __add__(self, node):
        if not issubclass(type(node), Node):
            raise ValueError('Not a Node')
        temp = self.header
        if temp is None:
            self.header = node
            return self
        while True:
            if temp.next is None:
                temp.next = node
                return self
            temp = temp.next

    @property
    def length(self):
        temp = self.header
        l = 0
        while temp is not None:
            temp = temp.next
            l = l + 1
        return l

    def __str__(self) -> str:
        s = ''
        temp = self.header
        while temp != None:
            s += str(temp.value) + ','
            temp = temp.next
        return s


if __name__ == "__main__":
    ll = LinkedList()
    ll + Node('123') + Node(9) + Node(6) + Node(6) + Node(13)
    print(ll)
