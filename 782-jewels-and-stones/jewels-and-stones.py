class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
#   Create hash table of jewel with each value being 0
        dict_jewel: {str: int} = {}
        for jewel in jewels:
            dict_jewel[jewel] = 0
#   Iterate through stones, if in hash table increment by 1
        for stone in stones:
            if stone in dict_jewel:
                dict_jewel[stone] += 1
#   Return sum of values in hash map
        return sum(dict_jewel.values())
