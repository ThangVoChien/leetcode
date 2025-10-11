class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for str in s:
            if str in ('(', '{', '['):
                stack.append(str)
            elif len(stack) == 0:
                return False
            else:
                p = stack.pop()
                if p + str not in ('()', '{}', '[]'):
                    return False

        if len(stack) == 0:
            return True
        else:
            return False