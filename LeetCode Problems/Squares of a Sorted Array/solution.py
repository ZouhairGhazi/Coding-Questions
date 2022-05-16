from pip import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer, right_pointer = 0, len(nums) - 1
        L = []
        while left_pointer <= right_pointer:
            if abs(nums[left_pointer]) >= abs(nums[right_pointer]):
                L.append(nums[left_pointer]**2)
                left_pointer += 1
            else:
                L.append(nums[right_pointer]**2)
                right_pointer -= 1
        return L[::-1]