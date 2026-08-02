class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        s=list(s)
        left = 0
        
        for i in range(len(t)):
            if t[i]==s[left]:
                left = left + 1
                if len(s) == left:
                    return True
            else:
                continue
        if left ==len(s):
            return True
        else:
            return False
        
