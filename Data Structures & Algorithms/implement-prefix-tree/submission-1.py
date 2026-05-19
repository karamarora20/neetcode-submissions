class PrefixTree:

    def __init__(self):
        self.root=Node()
    def insert(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if  ch not in curr.links:
                curr.links[ch]=Node()
            curr=curr.links[ch]
        curr.end=True
            
    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word:
            if  ch not in curr.links:
                return False
            curr=curr.links[ch]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix:
            if  ch not in curr.links:
                return False
            curr=curr.links[ch]
        return True
        
class Node:
    def __init__(self,end=False):
        self.links={}
        self.end=end  