class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base_to_anagrams: {str: List[str]} = {}

        for string in strs:
            split_string = list(string)
            split_string.sort()
            print(split_string)
            sorted_string = "".join(split_string)
            if sorted_string in base_to_anagrams:
                print(base_to_anagrams[sorted_string])
                base_to_anagrams[sorted_string].append(string)
            else:
                base_to_anagrams[sorted_string] = [string]
        
        return base_to_anagrams.values()