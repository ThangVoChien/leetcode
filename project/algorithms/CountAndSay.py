class Solution:
    memo = ["1"]
    def countAndSay(self, n: int) -> str:
        if n <= len(self.memo):
            return self.memo[n-1]
        
        c = self.countAndSay(n - 1)
        sol = ""
        
        count = 1
        for i in range(len(c)):
            if i != len(c)-1 and c[i] == c[i+1]:
                count+=1
            else:
                sol += str(count) + c[i]

                if i != len(c)-1:
                    count = 1

        self.memo.append(sol)
        return sol