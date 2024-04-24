from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
# Use Graph BFS to find least number of moves to get to end
# Need way to translate a value to the Boustrophedon layout of the matrix, will traverse matrix to develop hash table tracking values with coordinates
        boustro_hash = dict()
        board_size = len(board)
        is_even = (board_size - 1) % 2 == 0
        boustro_label = 1
        
        for row in reversed(range(board_size)):
            col_direction = range(board_size)
           
            if is_even:
                if row % 2 != 0:
                    col_direction = reversed(col_direction)
            else:   
                if row % 2 == 0:
                    col_direction = reversed(col_direction)

            for col in col_direction:
                    boustro_hash[boustro_label] = [row, col]
                    boustro_label += 1
        print(boustro_hash)      
        moves = list(range(1, 7))
        
        def is_valid(position: int) -> bool: 
            return position in boustro_hash
        
        def is_end(position: int) -> bool:
            return position == board_size * board_size
        
        seen = set()
        seen.add((board_size - 1, 0))
        
        queue = deque()
        queue.append([board_size - 1, 0, 1, 0])
 
        while queue:
            row, col, boustro_val, steps = queue.popleft()
            
            for move in moves:
                new_boustro_val= boustro_val + move
                
                if is_valid(new_boustro_val):
                    if is_end(new_boustro_val):
                        print('here2')
                        return steps + 1
                    
                    new_row, new_col = boustro_hash[new_boustro_val]
                    
                    if (new_row, new_col) not in seen:
                        seen.add((new_row, new_col))
                        if board[new_row][new_col] != -1:
                            if is_end(board[new_row][new_col]):
                                print('here')
                                return steps + 1
                            
                            row_after_slide, col_after_slide = boustro_hash[board[new_row][new_col]]
                            queue.append([row_after_slide, col_after_slide, board[new_row][new_col], steps + 1])
                        else:
                            queue.append([new_row, new_col, new_boustro_val, steps + 1])
                            
        return -1
        
        