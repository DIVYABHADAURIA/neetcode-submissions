class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in nums:
            if n - 1 not in num_set:
                len_seq = 1
                while n + len_seq in num_set:
                    len_seq += 1
                max_len = max(max_len, len_seq)

        return max_len
                
                    




        