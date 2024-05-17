class Solution:
    def maximum69Number (self, num: int) -> int:
# Largest number will have the most consecutive 9's as possible
# Should iterate from first digit and find the first 6 to change to a 9
        str_digit_array = list(str(num))
        for i in range(len(str_digit_array)):
            if str_digit_array[i] == '6':
                str_digit_array[i] = '9'
                return int(''.join(str_digit_array))
        
        return num
                
            