from typing import Optional
from dataStructures.BinaryTree import TreeNode
from dataStructures.LinkedList import ListNode

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def divide(head: ListNode):
            if head == None:
                return None
            elif head.next == None:
                return TreeNode(head.val)
            
            slow = head
            fast = head.next.next
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next

            node = TreeNode(slow.next.val)
            next = slow.next.next
            slow.next = None

            node.left = divide(head)
            node.right = divide(next)

            return node
        return divide(head)