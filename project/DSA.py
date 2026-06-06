from algorithms.ImplementStackUsingQueues import *
from dataStructures import *

# print(Solution().preorderTraversal(binaryTree([1])))
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())