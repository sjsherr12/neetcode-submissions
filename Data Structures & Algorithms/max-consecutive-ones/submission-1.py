class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        curr_length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_length += 1
            else:
                max_length = max(max_length, curr_length)
                curr_length = 0
        max_length = max(max_length, curr_length)
        return max_length