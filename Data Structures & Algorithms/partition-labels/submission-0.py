class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_of={c:i for i,c in enumerate(s)}
        end=0
        start=0
        ans=[]
        for i,c in enumerate(s):
            end=max(end,end_of[c])
            if i==end:
                ans.append(end+1-start)
                start=end+1
        return ans