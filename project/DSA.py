from algorithms.MinStack import *
from dataStructures import *

# print(Solution().maxProduct([-2]))
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())