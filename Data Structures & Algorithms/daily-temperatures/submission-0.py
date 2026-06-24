class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        sum=0
        for i in range(n):
             for j in range(i+1,n):
                    
                    if temperatures[j] > temperatures [i]:
                        sum = j-i
                        result[i] = sum
                        break
                    
                        
                        
        return result

        