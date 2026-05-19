class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.links:
                curr.links[ch]=Node()
            curr=curr.links[ch]
        curr.end=True

    def search_word(self,word):
        curr=self.root
        for ch in word:
            if ch not in curr.links:
                return False
            curr=curr.links[ch]
        return curr.end
    def search(self, word: str) -> bool:
        l=len(word)
        
        q=deque([(0,[],self.root)])
        candidates=[]
        while(q):
            idx,candidate,curr=q.popleft()
            if idx==l:
                candidates.append(''.join(candidate))
            else:
                if word[idx]!='.':
                    ch=word[idx]
                    if ch in curr.links:
                        q.append((idx+1,candidate+[ch],curr.links[ch]))
                else:
                    for key in curr.links:
                        q.append((idx+1,candidate+[key],curr.links[key]))
        for c in candidates:
            if self.search_word(c):
                return True
        return False
        

        
class Node:
    def __init__(self):
        self.links={}
        self.end=False