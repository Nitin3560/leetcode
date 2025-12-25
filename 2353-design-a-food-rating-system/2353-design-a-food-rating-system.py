class FoodRatings:
    def __init__(self,foods,cuisines,ratings):
        self.fc={}
        self.fr={}
        self.ch=defaultdict(list)
        for f,c,r in zip(foods,cuisines,ratings):
            self.fc[f]=c
            self.fr[f]=r
            heapq.heappush(self.ch[c],(-r,f))
    def changeRating(self,food,newRating):
        c=self.fc[food]
        self.fr[food]=newRating
        heapq.heappush(self.ch[c],(-newRating,food))
    def highestRated(self,cuisine):
        h=self.ch[cuisine]
        while True:
            r,f=h[0]
            if -r!=self.fr[f]:
                heapq.heappop(h)
            else:
                return f

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)