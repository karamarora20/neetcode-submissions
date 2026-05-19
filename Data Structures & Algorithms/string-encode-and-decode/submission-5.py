class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:
            if s=='':
                ans.append('`')
            else:
                ans.append(s)
        return '-'.join(ans)
        
    def decode(self, s: str) -> List[str]:
        ans=[]
        # s=s.split()
        for st in s.split('-'):
            if st=='':
                continue
            elif st=='`':
                ans.append('')
            else:
                ans.append(st)
        return ans
