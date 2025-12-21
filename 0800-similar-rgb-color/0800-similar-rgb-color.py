class Solution:
    def similarRGB(self, color: str) -> str:
        def closest(v: int) -> int:
            k = int(round(v / 17)) 
            k = max(0, min(15, k))  
            return 17 * k   

        def to_hex2(x: int) -> str:
            return f"{x:02x}"

        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)

        rr = closest(r)
        gg = closest(g)
        bb = closest(b)

        return "#" + to_hex2(rr) + to_hex2(gg) + to_hex2(bb)