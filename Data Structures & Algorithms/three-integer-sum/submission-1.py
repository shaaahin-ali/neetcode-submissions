class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=len(nums)
        rev=set()
        for i in range(s):
          for j in range(i+1,s):
            for k in range(j+1,s):
              if nums[i] + nums[j] + nums[k] == 0:
                triplet=tuple(sorted([nums[i], nums[j], nums[k]]))
                rev.add(triplet)
        return [list(t) for t in rev]
                
