from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = {}

        def greedy(n):
            if n in visited:
                return visited[n]
            if n == len(nums)-1:
                return True

            choice = []
            map = {}

            num = nums[n]
            if num == 0:
                return False

            for i in range(n + 1, n + num + 1):
                if i >= len(nums):
                    break
                if nums[i]+i in map:
                    continue

                choice.append(nums[i]+i)
                map[nums[i]+i] = i

            choice.sort(reverse=True)
            for c in choice:
                sol = greedy(map[c])
                visited[map[c]] = sol
                if sol != 0:
                    return True
            return False

        return greedy(0)
    
    def jump(self, nums: List[int]) -> int:
        visited = {}

        def greedy(n):
            if n in visited:
                return visited[n]
            if n == len(nums)-1:
                return 1

            choice = []
            num = nums[n]
            if num == 0:
                return 0

            for i in range(n + 1, n + num + 1):
                if i >= len(nums):
                    break
                if i == len(nums)-1:
                    return 2
                choice.append((nums[i]+i, i))

            choice.sort(reverse=True)
            for c in choice:
                sol = greedy(c[1])
                visited[c[1]] = sol
                if sol != 0:
                    return 1 + sol
            return 0

        return greedy(0)-1