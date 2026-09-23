class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums) - 1
        mid = (l+r)//2 
        min_num = nums[mid]

        while l <= r:
            mid = (l+r)//2 
            
            print("mid and min",mid,min_num)
            if nums[mid] >= nums[l]:
                min_num = min(min_num,nums[l])
                l = mid + 1
                #min_num = min(min_num,nums[l])
                print(min_num)
            
            else:
                r = mid 


            print(l,r)

        print(min_num)
        return min_num

        