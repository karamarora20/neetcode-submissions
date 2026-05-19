class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        nge=[n for _ in range(n)]
        st=[]
        for i in range(n-1,-1,-1):
            temp=temperatures[i]
            while(st and st[-1][1]<=temp):
                st.pop()
            if st:
                nge[i]=st[-1][0]
            st.append((i,temp))
        # print(nge)

        return [nge[i]-i if nge[i]<n else 0 for i in range(n)]


