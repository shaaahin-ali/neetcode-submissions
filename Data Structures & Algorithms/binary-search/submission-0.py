class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=len(nums)

        for i in range(s):
            if nums[i] == target:
                return i
                break
        return -1

        