class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.lower().split(" "))
        st,rev=[],[]
        for i in s:
            if i.isalnum():
                rev.insert(0,i)
                st.append(i)

        return rev==st

            
            