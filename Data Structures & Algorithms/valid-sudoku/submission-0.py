class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                value = board[i][j]
                box_index = (i//3) *3 + (j//3)

                if value == ".":
                    continue
                
                if value in rows[i] or value in cols[j] or value in box[box_index]:
                    return False
                
                rows[i].add(value)
                cols[j].add(value)
                box[box_index].add(value)
            

        return True





                