class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(max(len(v1), len(v2))):
            if i >= len(v1):
                i1 = 0
            else:
                i1 = int(v1[i])

            if i >= len(v2):
                i2 = 0
            else:
                i2 = int(v2[i])

            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1
        return 0