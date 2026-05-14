class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
            if counts[nums[i]] > math.floor(len(nums)/2):
                return nums[i]
        return 0