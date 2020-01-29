class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                results.append(abs(num))
            else:
                num[abs(num) - 1] = -(num[abs(num) - 1])
        return results

