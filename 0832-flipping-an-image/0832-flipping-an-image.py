class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            l=0
            h=len(r)-1
            while l<=h:
                r[l],r[h]=r[h]^1,r[l]^1
                l+=1
                h-=1
        return image







