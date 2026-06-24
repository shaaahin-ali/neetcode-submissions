class Solution:
    def maxArea(self, heights: List[int]) -> int:
        count= 0
        for i in range(len(heights)):
            for j in range (i + 1,len(heights)):
                width = j-i
                height = min(heights[i],heights[j])
                if width * height > count:
                    count = width * height
        return count