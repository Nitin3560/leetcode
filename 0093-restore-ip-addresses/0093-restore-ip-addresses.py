class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
    
        def valid(part: str) -> bool:
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) <= 255
    
        def dfs(i: int, parts: list):
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return
        
            remaining_parts = 4 - len(parts)
            remaining_chars = len(s) - i
            if remaining_chars < remaining_parts or remaining_chars > 3 * remaining_parts:
                return
        
            for l in range(1, 4):
                if i + l > len(s):
                    break
                seg = s[i:i+l]
                if valid(seg):
                    dfs(i + l, parts + [seg])
                if s[i] == '0':
                    break
    
        dfs(0, [])
        return res
