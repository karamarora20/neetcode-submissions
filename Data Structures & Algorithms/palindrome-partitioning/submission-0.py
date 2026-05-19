class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        n=len(s)
        def dfs(idx,palin):
            if idx==n:
                res.append(palin)
                return
            
            for i in range(idx+1,n+1):
                ss=s[idx:i]
                if ss==ss[::-1]:
                    dfs(i,palin+[ss])
               
        dfs(0,[])
        return res
            
            