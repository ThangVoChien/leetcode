from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self == None:
            return '[]'

        list = []

        s = '['
        list.append(self)
        while len(list) != 0:
            node = list.pop()
            s += str(node.val)
            if node.left != None:
                list.append(node.left)
            if node.right != None:
                list.append(node.right)
            if len(list) != 0:
                s += ', '
        s += ']'
        return s

def binaryTree(tree: List):
    root = TreeNode(val=tree[0])
    list = []
    list.append(root)
    
    i = 1
    while len(list) != 0:
        node = list.pop()

        if i < len(tree):
            if tree[i] != None:
                left = TreeNode(val=tree[i])
                node.left = left
                list.append(left)
            i+=1
        else:
            break

        if i < len(tree):
            if tree[i] != None:
                right = TreeNode(val=tree[i])
                node.right = right
                list.append(right)
            i+=1
        else:
            break

    return root