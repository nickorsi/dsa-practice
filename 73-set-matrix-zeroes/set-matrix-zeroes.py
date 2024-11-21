class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_locations: List[Tuple[int, int]] = []

        # First iterate through the matrix to find all the locations of 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_locations.append((row, col))

        # Then iterate through the locations and change every element in the row and col or that location to 0
        # Keep track  of rows and cols seen so duplicate work is avoided
        seen_rows: Set[int] = set()
        seen_cols: Set[int] = set()

        for zero_location in zero_locations: 
            row, col = zero_location
            if row not in seen_rows:
                seen_rows.add(row)
                for col_index in range(n):
                    matrix[row][col_index] = 0
            if col not in seen_cols:
                seen_cols.add(col)
                for row_index in range(m):
                    matrix[row_index][col] = 0
        