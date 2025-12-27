class StockPrice:

    def __init__(self):
        self.t2p={}
        self.tmax=0
        self.maxh=[]
        self.minh=[]

    def update(self, timestamp: int, price: int) -> None:
        self.t2p[timestamp]=price
        if timestamp>self.tmax:self.tmax=timestamp
        heapq.heappush(self.maxh,(-price,timestamp))
        heapq.heappush(self.minh,(price,timestamp))

    def current(self) -> int:
        return self.t2p[self.tmax]

    def maximum(self) -> int:
        while self.maxh:
            p,t=self.maxh[0]
            if self.t2p.get(t)==-p:return -p
            heapq.heappop(self.maxh)

    def minimum(self) -> int:
        while self.minh:
            p,t=self.minh[0]
            if self.t2p.get(t)==p:return p
            heapq.heappop(self.minh)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()