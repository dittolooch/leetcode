# run 3 iterations
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        results = []
        for num in nums:
            nums[abs(num) - 1] = abs(nums[abs(num) - 1])
        for i in range(len(nums)):
            if nums[i] < 0:
                results.append(i + 1)
        return results


# run 3 iterations
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        results = []
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                results.append(i + 1)
        return results
