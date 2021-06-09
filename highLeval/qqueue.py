#encoding: utf-8


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "Node({:d})".format(self.val)


class Qqueue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, n):
        if self.first is None:
            packNode = Node(n)
            self.first = packNode
            self.last = self.first
        else:
            packNode = Node(n)
            self.last.next = packNode
            self.last = packNode

    def dequeue(self):
        if self.first is Node:
            return None
        else:
            tmp = self.first.val
            self.first = self.first.next
            return tmp


if __name__ == '__main__':
    print("------ start ------")
    q = Qqueue()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    q.enqueue(n1)
    q.enqueue(n2)
    q.enqueue(n3)
    print(q.dequeue())
    print(q.dequeue())
    print("------ stop ------")
