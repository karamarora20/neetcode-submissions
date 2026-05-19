class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            # print(st)
            if t.isdigit() or (len(t)>1 and t[0]=='-'):
                st.append(int(t))
            elif t=='+':
                a,b=st.pop(),st.pop()
                st.append(b+a)
            elif t=='-':
                a,b=st.pop(),st.pop()
                st.append(b-a)
            elif t=='*':
                a,b=st.pop(),st.pop()
                st.append(b*a)
            elif t=='/':
                a,b=st.pop(),st.pop()
                st.append(int(b / a))
        return st[-1]