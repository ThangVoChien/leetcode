from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            s = "".join(sorted(str))
            if s not in dict:
                dict[s] = [str]
            else:
                dict[s].append(str)

        return list(dict.values())