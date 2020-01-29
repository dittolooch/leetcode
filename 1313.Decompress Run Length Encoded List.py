from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        results = []
        for ind, num in enumerate(nums):
            if ind % 2 == 0:
                freq = num
                ele = nums[ind + 1]
                components = [ele] * freq
                results += components
        return results


nums = [1, 2, 3, 4]
print(Solution().decompressRLElist(nums))
