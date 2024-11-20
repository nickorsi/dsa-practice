class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights) 
        n = len(heights[0])

        def is_valid_move(y:int, x:int)-> bool:
            return y < m and y >= 0 and x < n and x >= 0

        def check(effort: int) -> bool:
            moves = {(0,1), (0,-1), (1,0), (-1,0)}
            stack = [(0,0)]
            seen = {(0,0)}

            while stack:
                y, x = stack.pop()

                if y == m - 1 and x == n - 1: return True

                for dy, dx in moves:
                    ny = y + dy
                    nx = x + dx

                    if is_valid_move(ny, nx) and (ny, nx) not in seen:
                        if math.fabs(heights[y][x] - heights[ny][nx]) <= effort:
                            seen.add((ny, nx))
                            stack.append((ny, nx)) 

            return False

        left = 0
        right = max(max(arr) for arr in heights)
        
        while left <= right:
            mid = (right + left) // 2

            if check(mid):
                right = mid - 1
            else: 
                left = mid + 1

        return left
