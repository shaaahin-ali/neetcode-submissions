class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]

        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]
                ans = max(ans, current)

        return ans