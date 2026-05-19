class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1=[0]*26
        freq_s2=[0]*26
        a=ord('a')
        m=len(s1)
        n=len(s2)
        if n<m:
            return False
        for s in s1:
            freq_s1[ord(s)-a]+=1
        # for i in range(m):
        #     freq_s2[ord(s2[i])-a]+=1

        for i in range(n):
            if i>=m:
                freq_s2[ord(s2[i-m])-a]-=1
            freq_s2[ord(s2[i])-a]+=1
            if freq_s1==freq_s2:
                return True
        return False



        