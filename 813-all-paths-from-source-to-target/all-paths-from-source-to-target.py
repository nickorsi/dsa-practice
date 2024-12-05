class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Need to generate all possible paths from 0 to n - 1, where n = len(graph)
        possible_paths: List[List[int]] = []
            
        # Start at 0 always, then need to iterate through the potential paths from that node
        def backtrack(curr_path: List[int]) -> None:
            curr_node = curr_path[-1]
            # Base case is if current node == len(graph) - 1
            if curr_node == len(graph) - 1:
                # Add to possible_paths and return
                possible_paths.append(curr_path[:])
                return
            
            next_nodes = graph[curr_node]
            
            for next_node in next_nodes:
                # On each potential node, add to path and recurse
                curr_path.append(next_node)
                backtrack(curr_path)
                curr_path.pop()
                
        backtrack([0])
        return possible_paths