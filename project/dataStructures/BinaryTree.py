from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        if self == None:
            return '[]'

        list = []
        list.append(self)

        s = '['
        n = ''
        while len(list) != 0:
            node = list.pop(0)

            if node == None:
                n += ', null, '
            else:
                s += n + str(node.val)
                n = ''

                list.append(node.left)
                list.append(node.right)

                if len(list) != 0 and list[0] != None:
                    s += ', '
        s += ']'

        return s

def binaryTree(tree: List):
    if tree == None or len(tree) == 0:
        return None
    
    root = TreeNode(val=tree[0])
    list = []
    list.append(root)
    list.append(None)
    
    i = 1
    while len(list) != 0:
        node = list.pop(0)

        if i < len(tree):
            if tree[i] != None:
                left = TreeNode(val=tree[i])
                node.left = left
                list.append(left)
            i+=1

        if i < len(tree):
            if tree[i] != None:
                right = TreeNode(val=tree[i])
                node.right = right
                list.append(right)
            i+=1

        node.next = list[0]
        if list[0] == None:
            list.pop(0)
            if len(list) != 0:
                list.append(None)

    return root