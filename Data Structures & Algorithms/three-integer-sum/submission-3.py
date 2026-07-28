class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        t=0
        ans=[]
        dup = []
        for i in range(n):
          t = -nums[i]
          d={}
          for j in range(i+1,n):
            rem = t - nums[j]
            if rem in d:
              ans.append([nums[i],nums[d[rem]],nums[j]])
            d[nums[j]]= j 
        for tri in ans:
            if tri not in dup:
              dup.append(tri)
            else:
              continue
        
        return dup