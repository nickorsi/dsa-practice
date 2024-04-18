class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#       If source and destination are the same, return true
        if source == destination: return True
#       Will develop a hash map of nodes to neighbors
        nodes_to_neighbors: {int: List[int]} = {}
        
        for node1, node2 in edges:
            if node1 in nodes_to_neighbors:
                nodes_to_neighbors[node1].append(node2)
            else:
                nodes_to_neighbors[node1] = [node2]
            if node2 in nodes_to_neighbors:
                nodes_to_neighbors[node2].append(node1)
            else:
                nodes_to_neighbors[node2] = [node1]
#       Then do DFS traversal starting at node source to see if destination is ever reached while avoiding viewing an repeated nodes

        seen = set()
        # valid_path = False
        def dfs(n: int):
            if destination in nodes_to_neighbors[n]: 
                # nonlocal valid_path
                # valid_path = True
                return True
            if n not in seen:
                seen.add(n)
                for neighbor in nodes_to_neighbors[n]:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(source)
        
        # return valid_path
                
        
                