from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        moves = [(1,0), (-1,0), (0, 1), (0,-1)]
        start_m, start_n = entrance
    
        def is_valid(m: int, n: int) -> bool:
            return 0 <= m < len(maze) and 0 <= n < len(maze[0]) and maze[m][n] == '.'
        
        def is_exit(m: int, n: int) -> bool:
            return (m == 0 or m == len(maze) - 1 or n == 0 or n == len(maze[0]) - 1)
        
        queue = deque()
        queue.append([start_m, start_n, 0])

        seen = set()
        seen.add((start_m, start_n))

        while queue:
            m, n, curr_path = queue.popleft()

            for y, x in moves:
                new_m = m + y
                new_n = n + x
                if is_valid(new_m, new_n) and (new_m, new_n) not in seen:
                    if is_exit(new_m, new_n):
                        return curr_path + 1
                    seen.add((new_m, new_n))
                    queue.append([new_m, new_n, curr_path + 1])

        # while queue:
        #     m, n, curr_path = queue.popleft()
        #     seen.add((m, n))

        #     if not (m == entrance[0] and n == entrance[1]) and is_exit(m, n):
        #         return curr_path
        #     else:
        #         for y, x in moves:
        #             new_m = m + y
        #             new_n = n + x
        #             if is_valid(new_m, new_n) and (new_m, new_n) not in seen:
        #                 queue.append([new_m, new_n, curr_path + 1])
        #                 seen.add((new_m, new_n))
        return -1
            