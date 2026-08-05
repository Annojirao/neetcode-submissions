from math import ceil
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # arr_sum = int(((sorted(nums)[-1])) * (sorted(nums)[-1])+1))/2)
        # arr_sum = int((sorted(nums)[-1] * (sorted(nums)[-1] + 1)/2))
        arr_sum = int(len(nums) * (len(nums)+1)/2)
        return  arr_sum - sum(nums)
        