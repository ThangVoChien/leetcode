class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        s = ""

        z = 1000
        while num > 0:
            if num < z:
                z/=10
                continue
            
            n = num // z
            num %= z

            if n == 4 or n == 9:
                s += roman[z]
                n += 1

            if n == 10:
                s += roman[n*z]
            else:
                if n >= 5:
                    s += roman[5*z]
                    n -= 5
                
                s += roman[z] * int(n)
                z/=10

        return s