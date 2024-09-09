import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
       dict_count = Counter(words)

       list_count = [(-count, word) for word, count in dict_count.items()]

       heapq.heapify(list_count)

       return [heapq.heappop(list_count)[1] for _ in range(k)]
      
