class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ml = len(matrix[0]) - 1
        l = 0
        r = len(matrix) - 1
        i = -1
        while l <= r:
            m = (l + r)//2 
            if matrix[m][0] <= target <= matrix[m][ml]:
                i = m
                break
            elif target < matrix[m][0]:
                r = m - 1
            elif target >  matrix[m][ml]:
                l = m + 1
        if i == -1:
            return False
        l = 0
        r = len(matrix[i]) - 1
        while l <= r:
            m = (l + r)//2 
            if matrix[i][m] == target:
                return True
            elif target < matrix[i][m]:
                r = m - 1
            elif target >  matrix[i][m]:
                l = m + 1
        return False
        


        


        