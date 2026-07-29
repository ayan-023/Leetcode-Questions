class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s=s.lower().replace(" ","")
        s=re.sub(r'[^a-zA-Z0-9 ]', '', s)
        l=0
        r=(len(s))-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True