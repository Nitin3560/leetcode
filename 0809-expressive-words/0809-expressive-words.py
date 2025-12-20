class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def f(w):
            i=0
            j=0
            while i<len(s) and j < len(w):
                if s[i]!=w[j]:
                    return False
                a=i
                while a<len(s) and s[a] == s[i]:
                    a += 1
                b=j
                while b < len(w) and w[b] == w[j]:
                    b+=1
                x = a-i
                y = b-j
                if x != y and (x<3 or y> x):
                    return False
                i,j = a,b
            return i == len(s) and j ==len(w)

        return sum(f(w) for w in words)