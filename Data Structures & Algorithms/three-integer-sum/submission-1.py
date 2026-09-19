class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            target = -1 * nums[i]
            k = len(nums) - 1
            #print(j,k)

            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    k = k - 1
                    # Skip duplicate elements for the second number
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicate elements for the third number
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] > target:
                    k = k - 1
                else :
                    j = j + 1
        return res
                
                




