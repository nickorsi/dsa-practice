class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # // Brute Force Method: 
        # // Traverse entire board, ideally once
        # // Create maps for row, col, and grid checks
        #     // Keys will signify the number (row 1, col, 1, grid 1, etc) and values will be sets storing the numbers seen
        # // Anytime one of these maps are being updated and a duplicate exists

        row_values: Dict[int, Set[int]] = {} 
        col_values: Dict[int, Set[int]] = {} 
        grid_values: Dict[int, Set[int]] = {} 
       
        for row in range(len(board)):
            for col in range(len(board[0])):
                # print("row_values= ", row_values)
                # print("col_values= ", col_values)
                # print("grid_values= ", grid_values)
                # print("\n")
                current_value = board[row][col]
                if current_value == ".":
                    continue
                current_value_int = int(current_value)
                # print("current_value_int= ", current_value_int)
                # print("\n")
                grid_value = (row // 3) * 3 + (col // 3)
                # Check row
                if row in row_values:
                    values = row_values.get(row)
                    if current_value_int in values:
                        return False
                    values.add(current_value_int)
                    row_values[row] = values
                else:
                    row_values[row] = set([current_value_int])
                # Check col
                if col in col_values:
                    values = col_values.get(col)
                    if current_value_int in values:
                        return False
                    values.add(current_value_int)
                    col_values[col] = values
                else:
                    col_values[col] = set([current_value_int])
                # Check grid
                # (col // 3) * 3 + (row // 3) + 1 
                # Both row and col value go from 0 - 9 
                # 0 // 3 * 3 + 0 // 3 + 1 = 1
                # 2 // 3 * 3 + 2 // 3 + 1 = 1
                # 1 // 3 * 3 + 8 // 3 + 1 = 3
                if grid_value in grid_values:
                    values = grid_values.get(grid_value)
                    if current_value_int in values:
                        return False
                    values.add(current_value_int)
                    grid_values[grid_value] = values
                else:
                    grid_values[grid_value] = set([current_value_int])

        return True