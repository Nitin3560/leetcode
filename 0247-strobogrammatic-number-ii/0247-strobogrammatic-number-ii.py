class Solution:
#     def findStrobogrammatic(self, n: int) -> List[str]:
#         rot = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
#         res = []
#         def generate(curr):
#             if len(curr) == n:
#                 if n >1 and curr[0] == '0':
#                     return
#                 i =0
#                 j= n-1
#                 while i <= j:
#                     if curr[i] not in rot or rot[curr[i]] != curr[j]:
#                         return
#                     i += 1
#                     j-= 1
#                 res.append(curr)
#                 return
#             for d in '0123456789':
#                 generate(curr + d)

#         generate("")
#         return res

    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]
        def build(m, total):
            if m== 0:
                return [""]
            if m== 1:
                return ["0", "1", "8"]

            mids = build(m - 2, total)
            res =[]
            for mid in mids:
                for a, b in pairs:
                    if m== total and a == '0':
                        continue
                    res.append(a + mid + b)
            return res

        return build(n, n)