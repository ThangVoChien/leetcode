from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        addresses = []

        def backtrack(ip: List[str], pos):
            if pos == len(s):
                if len(ip) == 4:
                    addresses.append(".".join(ip))
                return
            if len(ip) == 4:
                return
            
            i = pos+1
            while i <= len(s):
                if i > pos+1 and s[pos] == "0":
                    break

                d = int(s[pos:i])
                if d >= 0 and d < 256:
                    ip.append(str(d))
                    backtrack(ip, i)
                    ip.pop()

                i+=1
        
        backtrack([], 0)
        return addresses