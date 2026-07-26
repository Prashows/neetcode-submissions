class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)

        cols = len(matrix[0])

        top = 0
        bot = row -1
        while top <= bot:

            row =  (top +bot)//2

            if  target > matrix[row][-1]:
                top = row +1 
                

            elif target <  matrix[row][0]:
                bot = bot -1

            else:
                break
        
        left = 0
        right = cols -1

        if not (top <= bot):
            return False
        
        row = (top +bot)//2
        while left <=right:

            m = (left + right)//2

            if target < matrix[row][m]:
                right = m-1
            
            elif target > matrix[row][m]:
                left = m+1 
            else:
                return True
        
        return False
