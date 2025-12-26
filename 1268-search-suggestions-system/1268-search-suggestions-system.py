class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        l=0
        r=len(products)
        prefix=""
        for ch in searchWord:
            prefix+=ch
            l=bisect_left(products,prefix,l,r)
            hi=prefix[:-1]+chr(ord(prefix[-1])+1)
            r=bisect_left(products,hi,l,r)
            res.append(products[l:min(l+3,r)])
        return res



