class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        heap = []

        for n in freq.keys():
            heapq.heappush(heap, (freq[n],n))
            if len(heap) > k:
                heapq.heappop(heap)

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
            
        
        

            

        