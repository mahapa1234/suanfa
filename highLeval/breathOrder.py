# encoding: utf8

from queue import Queue


class TreeNode (object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree (object):
    def __init__(self, root=None):
        self.root = root

    def breathSearch(self):
        if self.root is None:
            return None
        retList = []
        queue = Queue()
        queue.put(self.root)
        while queue.empty() is not True:
            node = queue.get()
            retList.append(node.val)
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        return retList


if __name__ == '__main__':
    rootNode = TreeNode(50)
    rootNode.left = TreeNode(20, TreeNode(15), TreeNode(30))
    rootNode.right = TreeNode(60, right=TreeNode(70))
    tree = BinaryTree(rootNode)
    retList = tree.breathSearch()
    print(retList)


