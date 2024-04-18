class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
#   Given an array of edges, which are UNDIRECTED, and number os nodes n
#   Must determine how many components are in the graph, IE distinct groups of nodes 
#   Can create hash of nodes to neighbors
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
#   Can then traverse graph using DFS and count how many times the recursive traversal needs to happen
        seen = set()
        ans = 0

        def dfs(node: int):
            if node not in seen:
                seen.add(node)
                for neighbor in node_hash[node]:
                    dfs(neighbor)

        for node in node_hash:
            if node not in seen:
                ans += 1
                dfs(node)
                
#   Return the number of traversals, which represents the number of distinct componenest

        return ans + n - len(node_hash)
        
            
