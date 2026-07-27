class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        n = len(nums)
        for i in range(n):
            if nums[i] in seen:
                seen.remove(nums[i])
            else:
                seen.append(nums[i])
        ans = seen[0]
        return ans