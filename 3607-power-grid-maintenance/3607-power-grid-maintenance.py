class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent=list(range(c+1))
        size=[1]*(c+1)
        def find(x:int)->int:
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(a:int,b:int)->None:
            ra,rb=find(a),find(b)
            if ra==rb:
                return
            if size[ra]<size[rb]:
                ra,rb=rb,ra
            parent[rb]=ra
            size[ra]+=size[rb]

        for u,v in connections:
            union(u,v)

        heaps={}
        online=[True]*(c+1)
        for i in range(1,c+1):
            r=find(i)
            if r not in heaps:
                heaps[r]=[]
            heapq.heappush(heaps[r],i)

        ans=[]
        for t,x in queries:
            if t==2:
                online[x]=False
            else:
                if online[x]:
                    ans.append(x)
                else:
                    r=find(x)
                    if r not in heaps:
                        ans.append(-1)
                        continue
                    h=heaps[r]
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    ans.append(h[0] if h else -1)
        return ans



