class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rw, cl = len(matrix),len(matrix[0]) 
        top, bot = 0, rw - 1
        row = -1
        #print("start",top,bot)
        while top <= bot:
            mid_row = (top + bot)//2
            #print("row",mid_row,top,bot)
            #print(target,matrix[mid_row][-1])
            if  target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif  target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                row = mid_row
                break
        if row == -1:
            return False
        #print(row,top,bot)en(matrix[0]) 
        l,r = 0,cl -1
        #print("left-right",l,r)

        while l <= r:
            mid = (l + r)//2
            #print(mid,matrix[row][mid],target)
            if matrix[row][mid] == target:
                return True
            elif target >  matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

            
            