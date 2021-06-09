# encoding: utf-8

"""
             11
       9           17
    6     10    12    19
 3    8

"""


class TreeNode (object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree (object):
    def __init__(self, root=None):
        self.root = root


# 先序遍历
def preOrder(retList, node):
    if node is not None:
        # 先访问根节点
        retList.append(node)
        preOrder(retList, node.left)
        preOrder(retList, node.right)
    return retList


# 中序遍历
def inOrder(retList, node):
    if node is not None:
        inOrder(retList, node.left)
        retList.append(node)
        inOrder(retList, node.right)
    return retList


# 后续遍历
def postOrder(retList, node):
    if node is not None:
        postOrder(retList, node.left)
        postOrder(retList, node.right)
        retList.append(node)
    return retList


if __name__ == '__main__':
    print('------二叉树的 先序遍历 演示开始------')
    rootNode = TreeNode(11)
    rootNode.left = TreeNode(9, left=TreeNode(6, left=TreeNode(3), right=TreeNode(8)), right=TreeNode(10))
    rootNode.right = TreeNode(17, left=TreeNode(12), right=TreeNode(19))
    bTree = BinaryTree(rootNode)
    ret = preOrder([], bTree.root)
    for i in ret:
        print(i.val, end=' ')
    print('\n------二叉树的 先序遍历 演示结束！！！------')

    print('------二叉树的 中序遍历 演示开始------')
    ret = inOrder([], bTree.root)
    for i in ret:
        print(i.val, end=' ')
    print('\n------二叉树的 中序遍历 演示结束！！！------')

    print('------二叉树的 后序遍历 演示开始------')
    ret = postOrder([], bTree.root)
    for i in ret:
        print(i.val, end=' ')
    print('\n------二叉树的 后序遍历 演示结束！！！------')