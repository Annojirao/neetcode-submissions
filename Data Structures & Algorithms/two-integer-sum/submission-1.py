class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, n in enumerate(nums):
            if target - nums[i] in sum_dict:
                return [sum_dict[target - nums[i]], i]
            print(sum_dict)
            sum_dict[nums[i]] = i
        return []
        