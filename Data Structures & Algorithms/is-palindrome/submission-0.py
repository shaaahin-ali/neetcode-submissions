class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean=[]
        for c in s:
            if c.isalnum():
                clean +=c.lower()
        l=len(clean)

     
            

        for i in range(l//2):
            
                if clean[i]==clean[l-i-1]:
                    continue

                else:
                    return False
        
        return True

            
            