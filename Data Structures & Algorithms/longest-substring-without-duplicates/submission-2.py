class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n=len(s)
        freq=[0]*128
        # a=ord('a')
        st=0
        e=0
        maxx=0
        # s=s.strip()
        while(e<n):
            # print(e)
            print(e)
            freq[ord(s[e])]+=1
            while(freq[ord(s[e])]>1):
                freq[ord(s[st])]-=1
                st+=1
            maxx=max(maxx,e-st+1)
            e+=1
        return maxx