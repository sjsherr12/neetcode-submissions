class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
                if length == 0:
                    return 0
            else:
                i += 1
        
        return len(nums)