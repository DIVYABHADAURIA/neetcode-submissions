class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            comp = target - n
            #print(seen,comp)
            if comp in seen:
                return [seen[comp],i]
            
            seen[n] = i

        #print(seen)
        

        