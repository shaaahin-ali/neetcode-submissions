class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      n = len(prices)
      sum=0
      for i in range(n):
        for j in range(i,n):
          if (prices[j] - prices[i]) > sum:
            sum =  prices[j] - prices[i]
      return sum

          