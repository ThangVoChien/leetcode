class Solution:
    def reverseWords(self, s: str) -> str:
        sa = [i for i in s.split(" ") if i.strip() != ""]
        sa.reverse()
        return " ".join(sa)