class Solution:
    def minSetSize(self, arr: List[int]) -> int:
# Want to continue to choose the most frequently occuring integers until at least half of length is gone
# Can make a freq counter, sort the values of the counter, then iterate through until less half or less of length is left
        freq_counter = {}
    
        arr_length = len(arr)
        
        half_arr_length = len(arr)/2
    
        for value in arr:
            if value in freq_counter:
                freq_counter[value] += 1
            else:
                freq_counter[value] = 1
                
        value_counts = list(freq_counter.values())
        
        value_counts.sort()
        
        ans = 0
        
        while arr_length > half_arr_length:
            arr_length = arr_length - value_counts.pop()
            ans += 1
            
        return ans