class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        e=0
        n=len(s)
        ans=0
        vis=set()
        while(e<n):
            while s[e] in vis:
                ans=max(ans,e-l)
                vis.remove(s[l])
                l+=1
            vis.add(s[e])
            e+=1
        ans=max(ans,e-l)
        return ans


