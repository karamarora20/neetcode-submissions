class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars=[0]*26
        a= ord('a')
        for ch in s:
            idx= ord(ch)-a
            chars[idx]+=1
        for ch in t:
            idx= ord(ch)-a
            chars[idx]-=1
            if chars[idx]<0: # early exit
                return False
        for i in range(26):
            if chars[i]!=0:
                return False
        return True