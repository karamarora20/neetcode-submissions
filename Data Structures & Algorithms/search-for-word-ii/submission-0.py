class Node:
    def __init__(self):
        self.links = {}
        self.end = False
        self.word = None   # store full word when ending


class Solution:
    def findWords(self, board, words):

        # Step 1: Build Trie
        root = Node()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.links:
                    curr.links[ch] = Node()
                curr = curr.links[ch]
            curr.end = True
            curr.word = word

        r, c = len(board), len(board[0])
        result = set()

        def dfs(i, j, node):
            ch = board[i][j]

            if ch not in node.links:
                return

            next_node = node.links[ch]

            if next_node.end:
                result.add(next_node.word)

            board[i][j] = "#"   # mark visited

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != "#":
                    dfs(ni, nj, next_node)

            board[i][j] = ch   # backtrack

        # Step 2: DFS from every cell
        for i in range(r):
            for j in range(c):
                dfs(i, j, root)

        return list(result)
