from typing import Optional
from dataStructures.BinaryTree import TreeNode

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def inorder(arr, root):
            if not root:
                return
            
            inorder(arr, root.left)
            arr.append(root.val)
            inorder(arr, root.right)

        self.arr = []
        self.i = 0

        inorder(self.arr, root)

    def next(self) -> int:
        ans = self.arr[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return len(self.arr) > self.i