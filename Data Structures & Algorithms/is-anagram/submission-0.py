class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=sorted(t)
        s=sorted(s)
        # for i in range(len(t)):
        #     if t[i] == s[i]:
        #         return True
        #     else:
        #         return False
        if s == t:
            return True
        else:
            return False
     