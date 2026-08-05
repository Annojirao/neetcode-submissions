class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_arr = [1] * len(nums)
        for i, ele in enumerate(nums):
            left_product = 1
            right_product = 1
            for j in range(i):
                left_product = left_product * nums[j]
            for k in range(i+1,len(nums)):
                right_product = right_product * nums[k]
            output_arr[i] = left_product * right_product

        return output_arr
        