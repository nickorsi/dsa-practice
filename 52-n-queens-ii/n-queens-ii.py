class Solution:
    # board: List[List[int]] = None
    flattened_board: List[int] = []
    solution_count: int = 0

    def totalNQueens(self, n: int) -> int:
    #     # Create a board of n x n with 0's
    #     board = [[0 for n in range(n)] for m in range(n)]
    #     for row in board:
    #         self.flattened_board = [*self.flattened_board, *row]
    #     # solution_count = 0

    #     def backtrack(board: List[List[int]], queen_count: int, start_el: int) -> None:
    #         # BASE: If queencount is n, increment count and return 
    #         # print("queen_count= ", queen_count)
    #         # print("board= ", board)
    #         # print("start_el= ", start_el)
    #         if queen_count == n:
    #             # print("\n")
    #             # print("**********HERE")
    #             # print("\n")
    #             self.solution_count += 1
    #             return
    #         # Iterate through the board, picking the empty spot on the board (0) to place a queen and replace that spot with 1
    #         for el in range(start_el, len(self.flattened_board)):
    #             row = el // n
    #             col = el % n
    #             if board[row][col] == 0:
    #                 # print("row= ", row)
    #                 # print("col= ", col)
    #                 # print("start board= ", board)
    #                 # Fill the board with 1's in all horinzontal, vertical and diagonal positions -> Need a function for this
    #                 # if self.check_and_fill_board(board, row, col, 1, True):
    #                 self.check_and_fill_board(board, row, col, 1)
    #                 # print("board after 1 fill= ", board)
    #                 queen_count += 1
    #                 # Recurse into the next backtrack equation passing in the updated board and queencount
    #                 backtrack(board, queen_count, el + 1)
    #                 self.check_and_fill_board(board, row, col, -1)
    #                 # print("board after 0 fill= ", board)
    #                 # print("\n")
    #                 queen_count -= 1
       
    #     backtrack(board, 0, 0)
    #     # Return count
    #     return self.solution_count

    # def check_and_fill_board(self, board: List[List[int]], start_row: int, start_col: int, fill_value: int) -> None:
    #     # print("\n")
    #     # print("Fill Board= ", board, "start_row= ", start_row, "start_col= ", start_col)
    #     # print("\n")
    #     # Iterate throught the board
    #     for row in range(len(board)):
    #         for col in range(len(board[0])):
    #             curr_value = board[row][col]
    #             # If currently in same row or col as the start, then replace value
    #             if row == start_row or col == start_col:
    #                 board[row][col] += fill_value
    #             # If currently in row "above" or "below" start
    #             if abs(row - start_row) != 0:
    #                 # If currently in col diagonal from start, the replace value
    #                 if col == start_col - abs(row - start_row) or col == start_col + abs(row - start_row):
    #                     board[row][col] += fill_value
    #     return

        # Above times out, can do this WITHOUT a board. 
        # Need to simply keep track of queens placed in rows, cols, diags and anti_diags
        # Queens can only occupy unique rows/cols/diags/anti_diags, otherwise will be in another attack path
        # So can assume the queen will be in a unique row and track as a number in recursion, the rest can be kept track of as sets
        def backtrack2(rows: int, cols: Set[int], diags: Set[int], anti_diags: Set[int]) -> None:
            # Base case is row == n
            if rows == n:
                self.solution_count += 1
                return
            for col in range(1, n + 1):
                diag = col - rows
                anti_diag = col + rows - n
                
                if ((col in cols) or
                    (diag in diags) or
                    (anti_diag in anti_diags)):
                    continue
                else:
                    cols.add(col)
                    diags.add(diag)
                    anti_diags.add(anti_diag)
                    backtrack2(rows + 1, cols, diags, anti_diags)
                    cols.remove(col)
                    diags.remove(diag)
                    anti_diags.remove(anti_diag)

            return
        # Need to start at 0 with rows (No game pieces) otherwise will double up final result
        backtrack2(0, set(), set(), set())
        return self.solution_count
        