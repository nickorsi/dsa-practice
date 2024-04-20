# from collections import deque

# class Solution:
#     def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
# # Given maze of size m x n made up of walls '+' and rooms '.' and starting point entrance
# # Must find shortest path to a room that is at the edge of a maze
# # Can only move horizontally or vertically
# # Use bfs to find shortest path
# # Define moves and is_valid function
#         moves = [(1,0), (-1,0), (0, 1), (0,-1)]
    
#         def is_valid(m: int, n: int) -> bool:
#             return 0 <= m < len(maze) and 0 <= n < len(maze[0]) and maze[m][n] == '.'
        
#         def is_exit(m: int, n: int) -> bool:
#             return (m == 0 or m == len(maze) - 1 or n == 0 or n == len(maze[0]) - 1) and maze[m][n] == '.'
        
# # Define seen as set and steps as 0
#         seen = set()
# # Traverse grid in BFS using queue
#         queue = deque([[*entrance, 0]])
#         print(queue)
#         while queue:
#             m, n, curr_path = queue.popleft()
#             seen.add((m, n))

#             if not (m == entrance[0] and n == entrance[1]) and is_exit(m, n):
#                 return curr_path
#             else:
#                 for y, x in moves:
#                     new_m = m + y
#                     new_n = n + x
#                     if is_valid(new_m, new_n) and (new_m, new_n) not in seen:
#                         queue.append([new_m, new_n, curr_path + 1])
                

#         return -1
            

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # Mark the entrance as visited since its not a exit.
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        
        # Start BFS from the entrance, and use a queue `queue` to store all 
        # the cells to be visited.
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            
            # For the current cell, check its four neighbor cells.
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                # If there exists an unvisited empty neighbor:
                if 0 <= next_row < rows and 0 <= next_col < cols \
                    and maze[next_row][next_col] == ".":
                    
                    # If this empty cell is an exit, return distance + 1.
                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1
                    
                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        # If we finish iterating without finding an exit, return -1.
        return -1