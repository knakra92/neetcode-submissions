class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        if len(prices) <= 1:
            return 0

        max_profit = max(prices[right] - prices[left], 0)

        while left < right and right < len(prices):
            current_profit = prices[right] - prices[left]

            max_profit = max(current_profit, max_profit)

            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit