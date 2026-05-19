class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort()
        st=[]
        for pos,speed in cars:
            time_to_target=(target-pos)/speed
            while(st and st[-1]<=time_to_target):
                st.pop()
            st.append(time_to_target)
        return len(st)