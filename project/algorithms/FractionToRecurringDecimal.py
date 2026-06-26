class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        flag = True
        if numerator < 0:
            numerator = -numerator
            flag = not flag
        if denominator < 0:
            denominator = -denominator
            flag = not flag

        map = {}

        q = []
        r = numerator
        while r != 0:
            if r in map and "." in map and map[r] > map["."]:
                i = map[r]
                q.insert(i, "(")
                q.append(")")
                break
            else:
                map[r] = len(q)
                if r < denominator:
                    q.append("0")
                else:
                    q.append(str(r // denominator))
                    r %= denominator
                r *= 10
                
                if r != 0 and "." not in map:
                    map["."] = len(q)
                    q.append(".")

        if not flag:
            q.insert(0, "-")

        return "".join(q)