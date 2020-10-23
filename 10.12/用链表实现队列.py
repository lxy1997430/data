class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def put(self,data):
        node = Node(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty link")
        else:
            node = self.front
            self.front = node.next
            node.next = None
        self.size -= 1
        return node

    def __repr__(self):
        current = self.front
        str = ""
        while current:
            str += "{} --> ".format(current)
            current = current.next
        return str + "end"

    def is_empty(self):
        return self.front is None

if __name__ == '__main__':
    q = LinkQueue()
    q.put(5)
    q.put(2)
    q.put(0)
    print(q)
    