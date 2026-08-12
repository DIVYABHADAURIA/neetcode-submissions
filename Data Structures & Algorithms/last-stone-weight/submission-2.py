import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            
            x = -heapq.heappop(heap) 
            y = -heapq.heappop(heap) 
            print(x,y)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(heap, -(y-x))
            else:
                heapq.heappush(heap, -(x-y))
        
        if len(heap)>0:
            return -heapq.heappop(heap) 
        else:
            return 0






        


        