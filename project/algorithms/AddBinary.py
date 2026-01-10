class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        sa = list(a)
        sb = list(b)
        r = 0

        i = len(sa)-1
        j = len(sb)-1
        while i >= 0 or j >= 0 or r:
            if i >= 0 and j >= 0:
                s = [str(int(sa[i]) + int(sb[j]) + r)] + s
            elif i >= 0:
                t = i
                while r:
                    if t < 0:
                        sa = ["1"] + sa
                        i+=1
                        break
                    else:
                        sa[t] = str(int(sa[t]) + r)
                        if sa[t] == "2":
                            sa[t] = "0"
                        elif sa[t] == "3":
                            sa[t] = "1"
                        else:
                            r = 0
                        t-=1
                s = sa[:i+1] + s
                break
            elif j >= 0:
                t = j
                while r:
                    if t < 0:
                        sb = ["1"] + sb
                        j+=1
                        break
                    else:
                        sb[t] = str(int(sb[t]) + r)
                        if sb[t] == "2":
                            sb[t] = "0"
                        elif sb[t] == "3":
                            sb[t] = "1"
                        else:
                            r = 0
                        t-=1
                s = sb[:j+1] + s
                break
            else:
                s = ["1"] + s

            if s[0] == "2":
                s[0] = "0"
                r = 1
            elif s[0] == "3":
                s[0] = "1"
                r = 1
            else:
                r = 0

            i-=1
            j-=1

        return "".join(s)