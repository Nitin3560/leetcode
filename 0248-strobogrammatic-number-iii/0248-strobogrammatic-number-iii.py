class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # m = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        # count =0
        # for num in range(int(low), int(high) + 1):
        #     s = str(num)
        #     l, r= 0, len(s) - 1
        #     ok= True

        #     while l<= r:
        #         if s[l] not in m or m[s[l]]!= s[r]:
        #             ok = False
        #             break
        #         l +=1
        #         r -=1

        #     if ok:
        #         count+= 1

        # return count
        
        pairs = [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]
        def generate(n, m):
            if n== 0:
                return [""]
            if n ==1:
                return ["0","1","8"]
            middle = generate(n-2, m)
            ans =[]
            for s in middle:
                for a, b in pairs:
                    if n ==m and a== '0':
                        continue
                    ans.append(a+s+b)
            return ans
        count =0
        for length in range(len(low), len(high) +1):
            nums =generate(length, length)
            for num in nums:
                if length == len(low) and num <low:
                    continue
                if length == len(high) and num >high:
                    continue
                count +=1
        return count