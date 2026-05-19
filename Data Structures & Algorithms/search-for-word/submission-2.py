class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r,c,i):
            if i==len(word):
                return True
            elif r==m or c==n or r<0 or c<0 or board[r][c]!=word[i]:
                return False
            
            board[r][c],temp='#',board[r][c]
            found= (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            board[r][c]=temp
            return found
            
        for r in range(m):
            for c in range(n):
                if board[r][c]==word[0] and dfs(r, c, 0):
                    return True
        
        return False