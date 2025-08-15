class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(n - 1):
            new_term = []
            count = 1
            for i in range(1, len(term) + 1):
                if i < len(term) and term[i] == term[i - 1]:
                    count += 1
                else:
                    new_term.append(str(count))
                    new_term.append(term[i - 1])
                    count = 1
            term = "".join(new_term)
        return term
