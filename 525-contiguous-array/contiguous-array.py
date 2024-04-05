class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
#   Input: Array of 0 or 1 'nums'
#   Output: Integer representing max length of array containing equal number of 0 and 1
#   Tricky, different way of approaching this problem than most
#   Need a way to track the number of 0's and 1's, can do this by a global count variable
#   This goes down by 1 if number is 0, goes up by 1 if 1
#   Can track index position where these count values first occur in a hash table
#   Can then compare similar count values later in the given array to where the count value first occured, this will given length of subarray that contains equal 0's and 1's
#   For this to work properly, MUST initialize the hash table with 0 count at index -1, as this is technically where count is first 0 and this will allow for correct calc of subarray length when count is 0 again.
        num_count: {int: int} = {0: -1}
        count = 0
        max_length = 0
        
        for i in range(len(nums)):
            count = count -1 if nums[i] == 0 else count + 1
            if count in num_count: 
                max_length = max(max_length, i - num_count[count]) 
            else:
                num_count[count] = i
        
        return max_length
                
      
        
        