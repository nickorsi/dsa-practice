class TrieNode:
    def __init__(self): 
        self.children = dict()
        self.is_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search_suggestions_from_prefix(self, prefix: str, result_count: int) -> List[str]:
        self.results = []
        node = self.root

        for char in prefix: 
            if char not in node.children:
                return []
            node = node.children[char]
                    
        def bfs(node: TrieNode, word: str, result_count: int) -> None:
            if len(self.results) == result_count:
                return
            if node.is_word:
                self.results.append(word)
            for char in node.children:
                new_word = word + char
                bfs(node.children[char], new_word, result_count)

        bfs(node, prefix, result_count)

        return self.results
        



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        product_trie = Trie()
        products.sort()
        results = []

        for product in products:
            product_trie.insert(product)

        prefix = ''
        for char in searchWord:
            prefix += char
            results.append(product_trie.search_suggestions_from_prefix(prefix, 3))

        return results
        