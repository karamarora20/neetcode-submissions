from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev,st=deque([]),deque([])
        s="".join(s.lower().split(" "))
        for i in s:
            if i.isalnum():
                rev.appendleft(i)
                st.append(i)

        return rev==st

            
            