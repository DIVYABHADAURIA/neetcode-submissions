class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum = len(nums) * [0]

        suffix = len(nums) * [0]

        res = len(nums) * [0]


        pre_sum[0] = suffix[len(nums) - 1] = 1
        for n in range(1,len(nums)):
            pre_sum[n] = pre_sum[n-1] * nums[n-1]

        for n in range(len(nums)-2,-1,-1):
            suffix[n] = suffix[n+1] * nums[n+1]

        for n in range(len(nums)):
            res[n] = suffix[n] * pre_sum[n]
            
        return res
        

        





            





