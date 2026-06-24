class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=len(numbers)
        for i in range(s):
            for j in range(s):
                if numbers[i] +numbers[j] == target:
                    return [i+1,j+1]
                

