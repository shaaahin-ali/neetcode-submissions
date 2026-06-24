class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     result=[]
     for i in range(len(nums)):
        s=1
        for j in range(len(nums)):
            if i!= j:
                s *=nums[j]
                
        result.append(s)
     return result

