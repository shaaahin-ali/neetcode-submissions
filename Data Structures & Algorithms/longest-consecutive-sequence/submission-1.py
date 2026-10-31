class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        s = 1
        longest = 1

        for i in range(len(nums) - 1):

            if nums[i+1] == nums[i] + 1:
                s += 1

            elif nums[i+1] == nums[i]:
                continue

            else:
                s = 1

            longest = max(longest, s)

        return longest