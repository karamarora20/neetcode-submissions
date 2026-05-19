class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        g=collections.defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+'*'+word[j+1:]
                g[pattern].append(word)

        transforms=1
        q=deque([beginWord])
        vis=set([beginWord])
        while(q):
            for j in range(len(q)):
                curr=q.popleft()
                if curr==endWord:
                    return transforms
                for i in range(len(curr)):
                    pattern=curr[:i]+'*'+curr[i+1:]
                    for nei in g[pattern]:
                        if nei not in vis:
                            q.append(nei)
                            vis.add(nei)
            transforms+=1
        return 0
        

