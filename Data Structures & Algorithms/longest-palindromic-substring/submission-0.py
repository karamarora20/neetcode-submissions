class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxx=0
        max_s=''
        for i in range(n):
            for j in range(i+1,n+1):
                sub_str=s[i:j]
                if sub_str==sub_str[::-1] and maxx<=j-i:
                    max_s=sub_str
                    maxx=j-i
                    
        return max_s