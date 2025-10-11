class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            while not s[start].isalnum():
                start+=1
                if start >= end:
                    break

            while not s[end].isalnum():
                end-=1
                if start >= end:
                    break

            if start >= end:
                break
            
            if s[start].lower() != s[end].lower():
                return False
            else:
                start+=1
                end-=1
            
        return True
    
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        deleted = False
        checked = []

        while start < end:
            while not s[start].isalnum():
                start+=1
                if start >= end:
                    break

            while not s[end].isalnum():
                end-=1
                if start >= end:
                    break

            if start >= end:
                break
            
            if s[start].lower() != s[end].lower():
                if deleted:
                    if checked == []:
                        return False
                    else:
                        start = checked[0]
                        end = checked[1]
                        checked = []
                        continue

                if s[start] != s[end-1]:
                    start+=1
                else:
                    if not deleted and s[end] == s[start+1]:
                        checked = [start+1, end]
                    end-=1

                deleted = True
            else:
                start+=1
                end-=1
            
        return True