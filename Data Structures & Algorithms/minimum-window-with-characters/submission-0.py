from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        freq_s=defaultdict(int)
        freq_t=defaultdict(int)

        def check_t():
            for key,val in freq_t.items():
                if freq_s[key]<val:
                    return False
            return True

        a=ord('a')
        for i in t:
            freq_t[i]+=1
        n = len(s)
        st = 0
        e = 0
        minn = float("inf")
        ans = ""
        while(e<n):
            freq_s[s[e]] += 1
            while(check_t()):
                if e-st+1<minn:
                    minn = e - st + 1
                    ans = s[st:e+1]
                freq_s[s[st]]-=1
                st+=1
            e+=1
        return ans
            


        
