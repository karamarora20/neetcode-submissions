from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.items= defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.items[key].append((value,timestamp))
        print(self.items)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.items and self.items[key]!=[]:
            l=0
            entries=self.items[key]
            h=len(entries)-1
            val=""
            while(l<=h):
                mid=(l+h)//2
                if entries[mid][1]<=timestamp:
                    val=entries[mid][0]
                    l=mid+1
                else:
                    h=mid-1
            return val

            
        return ""



            
        
