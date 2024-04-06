class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
# Need to compare cols to rows
# Can create dict of rows and cols, counting how often each occurs
    # Must save the seuence of numbers as the key, but must be immutable like a string or tuple in python
# Then loop through one of the dicts and getting product of occurance of the same sequence of numbers occuring

        def create_tuple(arr: List[int]) -> tuple(): 
            return tuple(arr)

        dict_rows: dict(tuple, int) = dict()
        dict_cols: dict(tuple, int) = dict()

        for row in range(len(grid)):
            row_tuple = create_tuple(grid[row])
            if row_tuple in dict_rows:
                dict_rows[row_tuple] += 1
            else:
                dict_rows[row_tuple] = 1
        
        for col in range(len(grid[0])):
            col_nums = []
            for row in range(len(grid)):
                col_nums.append(grid[row][col])
            col_tuple = create_tuple(col_nums)
            if col_tuple in dict_cols:
                dict_cols[col_tuple] += 1
            else:
                dict_cols[col_tuple] = 1
        print(dict_rows, dict_cols)
        ans = 0

        for row_tuple in dict_rows:
            if row_tuple in dict_cols:
                ans += dict_rows[row_tuple] * dict_cols[row_tuple]

        return ans