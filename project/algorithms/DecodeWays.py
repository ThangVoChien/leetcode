class Solution:
    def numDecodings(self, s: str) -> int:
        map = {}

        def dynamic(st):
            if st in map:
                return map[st]

            if len(st) == 0:
                map[st] = 1
                return 1
            if int(st[0]) <= 0:
                map[st] = 0
                return 0
            
            num = 0
            if len(st) >= 2 and (int(st[0]) == 1 or (int(st[0]) <= 2 and int(st[1]) <= 6)):
                num += dynamic(st[2:])
            num += dynamic(st[1:])

            map[st] = num
            return num
        
        return dynamic(s)