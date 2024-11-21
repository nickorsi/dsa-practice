class Solution:
    def intToRoman(self, num: int) -> str:
        # Build dictionary for value to symbol relations
        val_symbol_relations = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        # Split the int into an array of each integer
        str_decimals = list(str(num))
        # Only have to worry about nums from 1 to 3999
        # Loop through each decimal place and convert based on the given ruleset
        roman_num = ""
        decimal_place_conversion = len(str_decimals)
        length_decimal_relations = {
            1: 1,
            2: 10,
            3: 100,
            4: 1000
        }
        for str_decimal in str_decimals:
            decimal = int(str_decimal)
            decimal_place = length_decimal_relations[decimal_place_conversion]
            # If 4 or 9, use subtractive
            if decimal == 4:
                roman_num += val_symbol_relations[1 * decimal_place] 
                roman_num += val_symbol_relations[5 * decimal_place]
            
            if decimal == 9:
                roman_num += val_symbol_relations[1 * decimal_place]
                roman_num += val_symbol_relations[10 * decimal_place]

            # If 1 or 5, use direct number
            if decimal == 1:
                roman_num += val_symbol_relations[1 * decimal_place]

            if decimal == 5:
                roman_num += val_symbol_relations[5 * decimal_place]
            # If 2-3 add single value up
            if decimal >= 2 and decimal <= 3:
                for i in range(decimal):
                    roman_num += val_symbol_relations[1 * decimal_place]
            # If 6-8 subtract largest value (5) and add single values after
            if decimal >=6 and decimal <=8:
                # print("decimal= ", decimal)
                # print("decimal_place= ", decimal_place)
                # print("5 * decimal_place = ", 5 * decimal_place)
                roman_num += val_symbol_relations[5 * decimal_place]

                for i in range(decimal - 5):
                    roman_num += val_symbol_relations[1 * decimal_place]

            decimal_place_conversion -= 1

        return roman_num