class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        map = {}
        def dynamic(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i, j) in map:
                return map[(i, j)]
            
            if i < len(s1) and s1[i] == s3[k]:
                if dynamic(i+1, j, k+1):
                    map[(i, j)] = True
                    return True
                
            if j < len(s2) and s2[j] == s3[k]:
                if dynamic(i, j+1, k+1):
                    map[(i, j)] = True
                    return True
                
            map[(i, j)] = False
            return False
        
        return dynamic(0, 0, 0)