class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking function will progress through board where
        def backtrack(row: int, col: int, seen: Set[Tuple[int, int]], i: int) -> bool:
            # print("row= ", row)
            # print("col= ", col)
            # print("seen= ", seen)
            # print("i= ", i)
            # print("\n")
            # BASE CASE i == len word
            if i == len(word):
                return True
            # Possible moves are vertical.horizontal neighbors
            moves = [[0,1], [0,-1], [1,0], [-1,0]]
            for dy, dx in moves:
                new_row = row + dy
                new_col = col + dx
                # Each future cell can only be a valid and unseen move
                # Can only move on if it matches the letter at i
                if (
                    is_valid(new_row, new_col) and 
                    (new_row, new_col) not in seen and
                    board[new_row][new_col] == word[i]    
                ):
                    seen.add((new_row, new_col))
                    if backtrack(new_row, new_col, seen, i + 1):
                        return True
                    seen.remove((new_row, new_col))

            return False

        def is_valid(row, col) -> bool:
            return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
        
        # Need to progress through the graph one cell at a time to find the FIRST LETTER
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Once found, then enter backtracking function 
                if board[row][col] == word[0]:
                    # If True can return True
                    # test1 = (row, col,)
                    # test2 = set([test1])
                    # print("test1= ", test1)
                    # print("test2= ", test2)
                    if backtrack(row, col, set([(row, col)]), 1):
                        return True

        # Else return False
        return False