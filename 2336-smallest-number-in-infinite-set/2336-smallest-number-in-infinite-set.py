class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.added_back = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.added_back:
            num = heapq.heappop(self.added_back)
            self.in_heap.remove(num)
            return num
        
        num = self.smallest
        self.smallest += 1
        return num

    def addBack(self, num: int) -> None:

        if num < self.smallest and num not in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)