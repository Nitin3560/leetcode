class HitCounter:

    def __init__(self):
        self.q=deque()
        self.c=0

    def hit(self, t: int) -> None:
        if self.q and self.q[-1][0]==t:
            self.q[-1][1]+=1
        else:
            self.q.append([t,1])
        self.c+=1

    def getHits(self, t: int) -> int:
        while self.q and t-self.q[0][0]>=300:
            self.c-=self.q[0][1]
            self.q.popleft()
        return self.c

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)