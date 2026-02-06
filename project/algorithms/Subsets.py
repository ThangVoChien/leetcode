from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = []

        def generate(num: str):
            sol = []
            for i in range(len(num)-1,-1,-1):
                if num[i] == "1":
                    sol.append(nums[len(num)-1-i])
            sols.append(sol)

            if int(num, base=2) == (2**len(num))-1:
                return
            else:
                generate(f"{int(num, 2)+1:0{len(num)}b}")
        generate("0"*len(nums))

        return sols