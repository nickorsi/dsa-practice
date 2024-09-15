import decimal
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return "Denominator is zero, invalid"
        if numerator == 0:
            return "0"
        if numerator % denominator == 0 :
            return str(int(numerator / denominator))
        
        
        ans = ""
        if (numerator < 0 and denominator >= 0) or (denominator < 0 and numerator >=0):
            ans += "-"

        seen: List[(int, int)] = []

        ans += str(abs(numerator) // abs(denominator)) + "."
        decimal_string = ""
        new_num = (abs(numerator) % abs(denominator)) * 10
        new_denom = abs(denominator)

        while new_num:
            print(seen, new_num)
            quotient = new_num // new_denom
            if (new_num, quotient) in seen:
                index = seen.index((new_num, quotient))
                decimal_string = decimal_string[0:index] + "(" + decimal_string[index:] + ")"
                break
            seen.append((new_num, quotient))
            decimal_string += str(quotient)
            new_num = (new_num % new_denom) * 10

        return ans + decimal_string