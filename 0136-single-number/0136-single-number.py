class Solution(object):
    def singleNumber(self, nums):
        newlist = []
        for i in nums:
            if i not in newlist:
                newlist.append(i)
            else:
                newlist.remove(i)
        return newlist.pop()
