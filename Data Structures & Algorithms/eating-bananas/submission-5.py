
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res=r

        while l <= r:
            #print(l,r)
            k = (l + r)//2
            #print(k)
            total = 0
            for i in piles:
                total = total + math.ceil(float(i)/k)

            #print(total)
        
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
        
        return res
        



        




        