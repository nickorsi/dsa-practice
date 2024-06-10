class Trie:

    def __init__(self):
        self.word_hash = dict()

    def insert(self, word: str) -> None:
        if len(word) not in self.word_hash:
            self.word_hash[len(word)] = set()
        self.word_hash[len(word)].add(word)

    def search(self, word: str) -> bool:
        if len(word) in self.word_hash and word in self.word_hash[len(word)]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        word_hash_key = len(prefix)
        if len(self.word_hash) > 0:
            max_key = max(self.word_hash.keys())

            while word_hash_key <= max_key:
                if word_hash_key in self.word_hash:
                    for word in self.word_hash[word_hash_key]:
                        if word[:len(prefix):] == prefix:
                            return True
                word_hash_key += 1
        
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)