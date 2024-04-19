class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
# Given number of nodes n, edges between nodes as a list of list pairs, and restricted nodes as list
# Must find the max number of nodes that can be traversed without touching a restricted node
# Develop neighbors hash for all nodes and edges
        node_hash: {int: List[int]} = {}
        
        for node1, node2 in edges:
            if node1 in node_hash:
                node_hash[node1].append(node2)
            else:
                node_hash[node1] = [node2]
            if node2 in node_hash:
                node_hash[node2].append(node1)
            else:
                node_hash[node2] = [node1]
        
        self.path_count = 0
        restricted_set = set(restricted)
        seen = set()
# Traverse nodes using DFS
        def dfs(node: int):
# If node not seen, add it
            if node not in seen:
                seen.add(node)
# If node is not restricted, increment curr_path_count and recurse through it's neighbors
                if node not in restricted_set:
                    self.path_count += 1
                    for neighbor in node_hash[node]:
                        dfs(neighbor)
        dfs(0)    
# Return max_path_count
        return self.path_count