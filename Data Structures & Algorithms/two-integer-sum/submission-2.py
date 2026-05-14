class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        i = 0
        for num in nums:
            my_dict[num] = i
            i += 1
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in my_dict and my_dict[diff] != j:
                return[j, my_dict[diff]]
        return []