class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        conv=0
        max_freq=0
        maxx=0
        #    max_freq_char=''
        freq=[0]*26
        A=ord('A')
        st,e=0,0
        n=len(s)
        while(e<n):
            freq[ord(s[e])-A]+=1
            max_freq=max(freq[ord(s[e])-A],max_freq)
            while(e-st+1-max_freq>k):
                # maxx=max(e-st+1,maxx)
                freq[ord(s[st])-A]-=1
                st+=1
            maxx=max(maxx,e-st+1)
            e+=1
        return maxx

    
        
                

            