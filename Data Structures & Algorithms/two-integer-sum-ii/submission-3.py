class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=len(numbers)
        left = 0
        right = s-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if target == sum:
                return [left+1 , right+1]
            elif target < sum:
                right =  right - 1
            else:
                left = left + 1
                

