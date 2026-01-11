class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        st = []

        for s in stack:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if len(st) > 0:
                    st.pop()
            else:
                st.append(s)

        return "/" + "/".join(st)