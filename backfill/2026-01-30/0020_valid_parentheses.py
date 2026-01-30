class Solution:
    def isValid(self, s):
        st = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                if not st or st[-1] != pairs.get(ch, ""):
                    return False
                st.pop()
        return not st
