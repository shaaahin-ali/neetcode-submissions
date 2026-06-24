class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      n=len(prices)
      rev=[]
      for i in range(n):
        for j in range(i+1,n):
          s=prices[j]-prices[i]
          rev.append(s)
      rev.sort()
      
      l=len(rev)
      if l==0:
        return 0
      if rev[l-1] >= 0:
        return rev[l-1]
      else:
        return 0