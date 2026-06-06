from algorithms.ImplementQueueUsingStacks import *
from dataStructures import *

# print(Solution().preorderTraversal(binaryTree([1])))
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())