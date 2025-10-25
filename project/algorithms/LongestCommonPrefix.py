from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        pre = ""

        length = 200
        for s in strs:
            if len(s) < length:
                length = len(s)

        i = 0
        flag = False
        while i < length:
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    flag = True
                    break
            
            if flag:
                break
            else:
                pre += c
                i+=1

        return pre