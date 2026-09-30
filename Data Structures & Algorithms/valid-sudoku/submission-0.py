class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            rows = set()
            cols = set()
            square = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows:
                    return False
                else:
                    rows.add(board[i][j])

            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in cols:
                    return False
                else: 
                    cols.add(board[j][i])
            
            for j in range(len(board)):
                top_row = (i // 3) * 3
                top_col = (i % 3) * 3

                if board[top_row + j//3][top_col + j%3] == ".":
                    continue

                if board[top_row + j//3][top_col + j%3] in square:
                    return False
                else: 
                    square.add(board[top_row + j//3][top_col + j%3])

        return True
                

            

