class MinStack:

    def __init__(self):
        self.curr_minn=[float('inf')]
        self.st=[]


    def push(self, val: int) -> None:
        self.st.append(val)
        
        self.curr_minn.append(min(val,self.curr_minn[-1]))

    def pop(self) -> None:
            self.st.pop()
            self.curr_minn.pop()
        

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.curr_minn[-1]

        
