class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_diff_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in int_diff_map:
                return [int_diff_map[diff], i]
            int_diff_map[num] = i
        return