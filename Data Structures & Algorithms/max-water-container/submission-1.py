class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # count = 0
#
# for i in range(len(heights)):
#     for j in range(i + 1, len(heights)):
#         width = j - i
#         height = min(heights[i], heights[j])
#
#         if width * height > count:
#             count = width * height
#
# return count

        left = 0
        right = len(heights) - 1

        ans = 0

        while left < right:
            width = right - left
            h = min(heights[left], heights[right])

            ans = max(ans, width * h)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans