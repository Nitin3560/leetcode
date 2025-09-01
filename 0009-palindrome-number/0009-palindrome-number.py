class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup=x
        result=0
        while x>0:
            lastdigit=x%10
            x=x//10
            result=result*10+lastdigit

        return True if result==dup else False
    
