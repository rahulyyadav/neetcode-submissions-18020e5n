from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r >= rows or c >= cols or 
                board[r][c] != 'O' or (r, c) in visit):
                return
            visit.add((r, c))
            board[r][c] = 'T'  
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == 'O':
                    dfs(r, c)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
