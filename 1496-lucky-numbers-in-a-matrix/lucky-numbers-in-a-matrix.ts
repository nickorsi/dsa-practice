function luckyNumbers (matrix: number[][]): number[] {
    // Define luckyNums as a num array and minRow and maxCol as arrays of length m and n respectively filled with infinity_pos and infinity_neg respectively
    const luckyNums: number[] = [];
    const minRow: number[] = new Array(matrix.length).fill(Number.POSITIVE_INFINITY);
    const maxCol: number[] = new Array(matrix[0].length).fill(Number.NEGATIVE_INFINITY);
    // Iterate through row m
    for(let row = 0; row < matrix.length; row ++) {
        // Iterate through col n
        for(let col = 0; col < matrix[0].length; col ++) {
            // If value at matrix[m][n] is smaller than minRow[m] then replace
            if (matrix[row][col] < minRow[row]) minRow[row] = matrix[row][col];
            // If value at matrix[m][n] is larger than maxcol[n] then replace
            if (matrix[row][col] > maxCol[col]) maxCol[col] = matrix[row][col];
        }
    }
    // Iterate through minRow
    for(const num of minRow) {
        // If in maxCol push into luckyNums
        if(maxCol.includes(num)) luckyNums.push(num);
    }
    // Return luckyNums
    return luckyNums;
};