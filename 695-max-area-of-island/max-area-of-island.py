class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         Given grid of size m x n
#         Valid square is on the grid and equal to 1
#         Need to iterate through grid a determine the largest sized island without revisiting squares
#         An island is made up of 1's that are touching vertically or horizontally, not diagonally
#         Create max_island_size as negative inf    
        max_island_size = 0
#         Create curr_island_size as 0
        curr_island_size = 0
#         Create a seen matrix filled with false values
        seen = []
        
        for m in range(len(grid)):
            seen_row = []
            for n in range(len(grid[0])):
                seen_row.append(False)
            seen.append(seen_row)
#         Create a valid_moves array
        valid_moves = [[1,0], [-1,0], [0,1], [0,-1]]
#         Create a is_valid function making sure coordinates are within grid
        def is_valid(m:int, n:int) -> bool:
            return 0 <= m < len(grid) and 0 <= n < len(grid[0])
#         Create a find_island_size that takes in coordinates and recursively applies valid moves to see if tile hasn't been seen and is valid
        def find_island_size(m: int, n: int):
            nonlocal seen
            nonlocal curr_island_size
            for y, x in valid_moves:
                new_m = m + y
                new_n = n + x
                if is_valid(new_m, new_n):
                    if not seen[new_m][new_n]:
                        seen[new_m][new_n] = True
                        if grid[new_m][new_n] == 1:
                            curr_island_size += 1
                            find_island_size(new_m, new_n)
#         Iterate through grid, if 1 then increment curr_island and enter find_island_size
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                # print(m, n, seen[m][n])
                if not seen[m][n]:
                    seen[m][n] = True
                    if grid[m][n] == 1:
                        curr_island_size += 1
                        find_island_size(m, n)
                        max_island_size = max(max_island_size, curr_island_size)
                        curr_island_size = 0
#         Return max_island_size
        return max_island_size