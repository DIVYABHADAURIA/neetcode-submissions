class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #print(len(matrix))
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False
            
        