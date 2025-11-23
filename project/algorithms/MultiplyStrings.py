class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        sol = 0
        for n1 in range(len(num1)-1, -1, -1):
            n = 0

            d1 = dict[num1[n1]]
            for n2 in range(len(num2)-1, -1, -1):
                d2 = dict[num2[n2]]

                d = d1 * d2
                n += d * 10 ** (len(num2)-1 - n2)

            sol += n * 10 ** (len(num1)-1 - n1)

        return str(sol)