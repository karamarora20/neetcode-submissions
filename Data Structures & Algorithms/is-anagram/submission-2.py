class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars=[0]*26
        a= ord('a')
        for ch in s:
            chars[ord(ch)-a]+=1
        for ch in t:
            chars[ord(ch)-a]-=1
            if chars[ord(ch)-a]<0: # early exit
                return False
        for i in range(26):
            if chars[i]!=0:
                return False
        return True