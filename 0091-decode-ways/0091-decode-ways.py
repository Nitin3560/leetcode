class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':return 0
        a=1;b=1
        for i in range(1,len(s)):
            c=0
            if s[i]!='0':c+=b
            if s[i-1]!='0' and 10<=int(s[i-1:i+1])<=26:c+=a
            a=b;b=c
            if b==0:return 0
        return b
 