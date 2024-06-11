# # Version 1
# class Trie:

#     def __init__(self):
#         self.word_hash = dict()

#     def insert(self, word: str) -> None:
#         if len(word) not in self.word_hash:
#             self.word_hash[len(word)] = set()
#         self.word_hash[len(word)].add(word)

#     def search(self, word: str) -> bool:
#         if len(word) in self.word_hash and word in self.word_hash[len(word)]:
#             return True
#         return False

#     def startsWith(self, prefix: str) -> bool:
#         word_hash_key = len(prefix)
#         if len(self.word_hash) > 0:
#             max_key = max(self.word_hash.keys())

#             while word_hash_key <= max_key:
#                 if word_hash_key in self.word_hash:
#                     for word in self.word_hash[word_hash_key]:
#                         if word[:len(prefix):] == prefix:
#                             return True
#                 word_hash_key += 1
        
#         return False

# Version 2
class trie_node:
    def __init__ (self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = trie_node()
    
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = trie_node()
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
                
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)