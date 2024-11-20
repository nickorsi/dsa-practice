class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) # m is ROW n is COL
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (right + left) // 2
            # How to get row and col from mid? 
            row = mid // n
            col = mid % n 
            # print(m, n)
            # print(left, right, mid, row, col)
            if matrix[row][col] == target: return True
            if matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False 
