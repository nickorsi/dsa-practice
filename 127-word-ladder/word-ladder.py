class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
# Need shortest path from beginWord to endWord if it exists, will used bfs and return 0 if doesn't exist, so must use a queue
# Does a hash need to be made? Don't think so. 
# Allowable transformation is a single letter, which must be lower case and part of english alph
#         def create_new_words(word: str) -> List[str]:
#             new_words = []
#             new_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#             for i in range(len(word)):
#                 for letter in new_letters:
#                     if word[i] != letter:
#                         new_word = word[:i] + letter + word[i+1:]
#                         if new_word in wordList and new_word not in self.seen:
#                             self.seen.add(new_word)
#                             new_words.append(new_word)
        
#             return new_words
                            
#         queue = collections.deque()
#         queue.append((beginWord, 1))
#         self.seen = set()
        
#         while queue:
#             curr_word, ladder_count = queue.popleft()
            
#             if curr_word == endWord:
#                 return ladder_count
            
#             for new_word in create_new_words(curr_word):
#                 queue.append((new_word, ladder_count + 1))
                
#         return 0
        
# Above is timing out, what if a hash map was created to map all neighbors and then this hash was traversed with BFS?
        # full_wordList = [beginWord, *wordList]
        # word_list_hash = dict()
        # for word in full_wordList:
        #     word_neighbors = []
        #     for i in range(len(full_wordList)):
        #         if word == full_wordList[i]:
        #             continue
        #         letter_diff = 0
        #         for j in range(len(beginWord)):
        #             if letter_diff > 1:
        #                 break
        #             if word[j] != full_wordList[i][j]:
        #                 letter_diff += 1
        #         if letter_diff < 2:
        #             word_neighbors.append(full_wordList[i])
        #     word_list_hash[word] = word_neighbors
            
        # queue = collections.deque()
        # queue.append((beginWord, 1))
        # seen = set()
        # seen.add(beginWord)
        
        # while queue:
        #     curr_word, ladder_count = queue.popleft()
            
        #     if curr_word == endWord:
        #         return ladder_count
            
        #     for neighbor in word_list_hash[curr_word]:
        #         if neighbor not in seen:
        #             seen.add(neighbor)
        #             queue.append((neighbor, ladder_count + 1))
                
        # return 0       
   
                
# Still timing out, looking at solution they save words to letter combos in a hash and traverse this way

        letter_word_hash = dict()

        for word in wordList:
            for i in range(len(beginWord)):
                letter_combo = word[:i] + '*' + word[i + 1:]
                if letter_combo in letter_word_hash:
                    letter_word_hash[letter_combo].append(word)
                else:
                    letter_word_hash[letter_combo] = [word]
        print(letter_word_hash)
        queue = collections.deque()
        queue.append((beginWord, 1))
        seen = set()
        seen.add(beginWord)
        
        while queue:
            curr_word, ladder_count = queue.popleft()
            
            if curr_word == endWord:
                return ladder_count
            
            for i in range(len(beginWord)):
                letter_combo = curr_word[:i] + '*' + curr_word[i+1:]
                
                if letter_combo in letter_word_hash:
                    for neighbor in letter_word_hash[letter_combo]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append((neighbor, ladder_count + 1))
                
        return 0    
                