
class TaskManager:
    def __init__(self,tasks:List[List[int]]):
        self.mp={}
        self.ver=0
        self.h=[]
        for u,tid,p in tasks:
            self.add(u,tid,p)

    def add(self,userId:int,taskId:int,priority:int)->None:
        self.ver+=1
        self.mp[taskId]=(userId,priority,self.ver,True)
        heapq.heappush(self.h,(-priority,-taskId,self.ver,taskId))

    def edit(self,taskId:int,newPriority:int)->None:
        u,_,_,_=self.mp[taskId]
        self.ver+=1
        self.mp[taskId]=(u,newPriority,self.ver,True)
        heapq.heappush(self.h,(-newPriority,-taskId,self.ver,taskId))

    def rmv(self,taskId:int)->None:
        u,p,v,_=self.mp[taskId]
        self.mp[taskId]=(u,p,v,False)

    def execTop(self)->int:
        while self.h:
            _,_,v,tid=heapq.heappop(self.h)
            if tid not in self.mp:
                continue
            u,p,cv,alive=self.mp[tid]
            if not alive or cv!=v:
                continue
            del self.mp[tid]
            return u
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()