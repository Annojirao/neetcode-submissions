class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        new_dict = dict()
        for i in range(length):
            diff = target - nums[i]
            if diff in new_dict.keys():
                return [new_dict[diff], i]
            else:
                new_dict[nums[i]] = i
        return []