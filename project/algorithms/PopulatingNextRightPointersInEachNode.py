from typing import Optional
from dataStructures.BinaryTree import TreeNode as Node


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root == None:
            return root

        list = []
        list.append(root)
        list.append(None)
        
        while len(list) != 0:
            node = list.pop(0)

            if node.left != None:
                list.append(node.left)
            if node.right != None:
                list.append(node.right)

            node.next = list[0]
            if list[0] == None:
                list.pop(0)
                if len(list) != 0:
                    list.append(None)

        return root