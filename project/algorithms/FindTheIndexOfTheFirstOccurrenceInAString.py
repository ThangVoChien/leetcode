class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        pt1 = 0
        pt2 = 0

        while pt1 < len(haystack):
            if len(haystack) - pt1 < len(needle):
                return -1
            
            p = pt1
            while haystack[p] == needle[pt2]:
                p+=1
                pt2+=1

                if pt2 == len(needle):
                    return pt1
                if p == len(haystack):
                    return -1
                
            pt1+=1
            pt2 = 0

        return -1