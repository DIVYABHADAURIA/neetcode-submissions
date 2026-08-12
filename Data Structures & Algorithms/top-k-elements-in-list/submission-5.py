from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        
        for n in nums:
            mp[n] = mp.get(n,0) + 1
        #print(mp)
        #print(Counter(nums))
        hp = []

        for n,count in mp.items():
            if len(hp) < k:
                heapq.heappush(hp,(count,n))
            else:
                heapq.heappushpop(hp,(count,n))

        return [item[1] for item in hp]

                
        

        