class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars={ch:i for i,ch in enumerate('abcdefghijklmnopqrstuvwxyz')}
        groups={}
        ans=[]
        for s in strs:
            key=[0]*26
            for ch in s:
                key[ord(ch)-ord('a')]+=1
            if tuple(key) in groups:
                groups[tuple(key)].append(s)
            else:
                groups[tuple(key)]=[s]
        for group in groups.values():
            ans.append(group)
        return ans

