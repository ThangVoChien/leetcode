class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dynamic(word, i):
            if word == word2:
                return 0
            if word in memo:
                return memo[word]
            else:
                memo[word] = 1000000000

            start = 0
            end = len(word)
            if i < end and i < len(word2) and word[i] == word2[i]:
                i = start
                while i < end and i < len(word2):
                    if word[i] != word2[i]:
                        break
                    i+=1

            iStep = abs((len(word)+1) - len(word2)) + 1
            dStep = abs((len(word)-1) - len(word2)) + 1
            rStep = abs(len(word) - len(word2)) + len(word2) - i 

            iSol = 999999999
            if i < len(word2) and iStep < rStep:
                iSol = dynamic(word[start:i] + word2[i] + word[i:end], i+1)
            dSol = 999999999
            if dStep <= rStep:
                dSol = dynamic(word[start:i] + word[i+1:end], i)
            rSol = 999999999
            if i < len(word2):
                rSol = dynamic(word[start:i] + word2[i] + word[i+1:end], i+1)

            memo[word] = min(iSol, dSol, rSol) + 1
            return memo[word]
        return dynamic(word1, 0)