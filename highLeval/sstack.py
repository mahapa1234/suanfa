# encoding: utf-8


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "Node({:d})".format(self.val)


class Sstack(object):
    def __init__(self):
        self.top = None

    def peek(self):
        if self.top is not None:
            return self.top.val
        else:
            return None

    def pop(self):
        if self.top is None:
            return None
        else:
            tmp = self.top.val
            self.top = self.top.next
            return tmp

    def push(self, node):
        if node is not None:
            packNode = Node(node)
            packNode.next = self.top
            self.top = packNode
            return packNode.val
        else:
            return None


if __name__ == '__main__':
    print("------ start ------")
    a = Node(1)
    b = Node(2)
    c = Node(3)
    s = Sstack()
    s.push(a)
    s.push(b)
    s.push(c)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("------ stop ------")