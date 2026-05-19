class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s={}
        char_t={}
        if len(s)!=len(t):
            return False
        for ch1,ch2 in zip(s,t):
            char_s[ch1]=char_s.get(ch1,0)+1
            char_t[ch2]=char_t.get(ch2,0)+1

        for char in char_t.keys():
            if char not in char_s or  char_t[char]!=char_s[char]:
                return False
        return True