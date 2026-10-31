class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean=[]
        for c in s:
            if c.isalnum():
                clean +=c.lower()
        l=len(clean)

     
            

        return clean[::-1]==clean

            
            