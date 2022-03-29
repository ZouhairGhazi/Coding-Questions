class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix_products = [1] * size
        suffix_products = [1] * size 
        
        prefix_products[0] = nums[0]
        suffix_products[0] = nums[size-1]
        
        for i in range(1, size): 
            prefix_products[i] = nums[i] * prefix_products[i-1]
            
        for i in range(1, size): 
            suffix_products[i] = nums[size-1-i] * suffix_products[i-1]
            
        S = [suffix_products[size-2]]
        for i in range(1, size-1):
            S.append(prefix_products[i-1]*suffix_products[size-i-2])
        S.append(prefix_products[size-2])
        
        return S
        