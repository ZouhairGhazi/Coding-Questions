class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxPrice = 0
        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
            else:
                maxPrice = max(maxPrice, prices[right] - prices[left])
            right += 1
        return maxPrice
            