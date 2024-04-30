class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
# Like a graph problem, each element in the array has links to up to two other elements, could have circlular relations
# Can traverse either BFS or DFS, will try DFS using recursion
        self.seen = set()
        self.seen.add(start)
        self.ans = False
        
        def bfs(node: int) -> bool:
            if arr[node] == 0:
                self.ans = True
                return
            forward = node + arr[node]
            backward = node - arr[node]
            
            if forward not in self.seen and 0 <= forward < len(arr):
                self.seen.add(forward)
                bfs(forward)
            if backward not in self.seen and 0 <= backward < len(arr):
                self.seen.add(backward)
                bfs(backward)
        
        bfs(start)
        
        return self.ans
            
        
    