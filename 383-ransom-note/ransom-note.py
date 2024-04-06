class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        dict_ransom: {str: int} = {}
        dict_magazine: {str: int} = {}
        
        for char in ransomNote:
            if char in dict_ransom: dict_ransom[char] += 1
            else: dict_ransom[char] = 1
            
        for char in magazine:
            if char in dict_magazine: dict_magazine[char] += 1
            else: dict_magazine[char] = 1
            
        for char in dict_ransom:
            if char not in dict_magazine: return False
            if dict_magazine[char] < dict_ransom[char]: return False
        
        return True
            
        