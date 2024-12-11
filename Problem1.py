# Problem 1: Arithmetic Slices
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0
        count = 0

        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                count += curr
            else:
                curr = 0

        return count