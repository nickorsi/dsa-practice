from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
# Need to find shortest # of mutations to get from start to end
# If the endGene isn't in bank, can instantly return -1
        if endGene not in bank: 
            return -1
# Mutation is changing 1 character at a time
        def gene_mutations(gene: str) -> List[str]:
            mutations = ["A", "C", "G", "T"]
            valid_mutations = []
            for i in range(len(gene)):
                for mutation in mutations:
                    new_mutation = gene[:i] + mutation + gene[i+1:]
                    print(new_mutation)
# Can only progress through valid mutations, which are held in bank
                    if new_mutation in bank:
                        valid_mutations.append(new_mutation)
            return valid_mutations
# Can progress through mutations doing BFS using a queue
        queue = deque()
        queue.append((startGene, 0))
        seen = set()
        
        while queue:
            curr_gene, mutation_count = queue.popleft()
# If at any time during queue progression the mutation is the end, return steps            
            if curr_gene == endGene:
                return mutation_count
            
            if curr_gene not in seen:
                seen.add(curr_gene)
                
                for mutation in gene_mutations(curr_gene):
                    queue.append((mutation, mutation_count + 1))            
# Otherwise if through all possible mutations, return -1
        print('here')    
        return -1