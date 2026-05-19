class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words=set(wordList)
        q=deque([beginWord])
        transforms=1
        if endWord not in words:
            return 0
        while(q):
            for j in range(len(q)):
                curr=q.popleft()
                if curr==endWord:
                    return transforms
                for i in range(len(curr)):
                    for ch in'abcdefghijklmnopqrstuvwxyz':
                        new_word=curr[:i]+ch+curr[i+1:]
                        if new_word in words:
                            q.append(new_word)
                            words.remove(new_word)
            transforms+=1
        return 0
        

