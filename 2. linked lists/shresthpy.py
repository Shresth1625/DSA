class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_tail(self, value):
        # new node
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

        # increment size
        self.size += 1

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.data) + ','
            current_node = current_node.next
        return result[:-1]

    def insert_mid(self, after_value, value):
        new_node = Node(value)
        current_node = self.head
        while current_node is not None:
            if current_node.data == after_value:
                break
            current_node = current_node.next
        if current_node is not None:
            new_node.next = current_node.next
            current_node.next = new_node
            self.size += 1
        else:
            return 'Item not found'

    def remove(self, value):
        if self.head is None:
            return 'Empty'
        if self.head.data == value:
            return self.delete_head()
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == value:
                break
            current_node = current_node.next
        if current_node.next is None:
            return 'Not Found'
        else:
            current_node.next = current_node.next.next
            self.size -= 1

    def clear(self):
        self.head = None
        self.size = 0

L_L = LinkedList()
for i in range(10):
    L_L.insert_tail(i)
print(L_L)

L_L.insert_mid(8, 12)
print(L_L)

L_L.remove(8)
print(L_L)
