function luckyNumbers (matrix: number[][]): number[] {
    // // Define luckyNums as a num array and minRow and maxCol as arrays of length m and n respectively filled with infinity_pos and infinity_neg respectively
    // const luckyNums: number[] = [];
    // const minRow: number[] = new Array(matrix.length).fill(Number.POSITIVE_INFINITY);
    // const maxCol: number[] = new Array(matrix[0].length).fill(Number.NEGATIVE_INFINITY);
    // // Iterate through row m
    // for(let row = 0; row < matrix.length; row ++) {
    //     // Iterate through col n
    //     for(let col = 0; col < matrix[0].length; col ++) {
    //         // If value at matrix[m][n] is smaller than minRow[m] then replace
    //         if (matrix[row][col] < minRow[row]) minRow[row] = matrix[row][col];
    //         // If value at matrix[m][n] is larger than maxcol[n] then replace
    //         if (matrix[row][col] > maxCol[col]) maxCol[col] = matrix[row][col];
    //     }
    // }
    // // Iterate through minRow
    // for(const num of minRow) {
    //     // If in maxCol push into luckyNums
    //     if(maxCol.includes(num)) luckyNums.push(num);
    // }
    // // Return luckyNums
    // return luckyNums;
    // Above it O(n*m) can it be done better? Have to traverse the whole matrix, BUT can do this greedily knowing that only 1 luckyNum can exist (see the editorial for explanation).
    // Want the lowest colMax and highest rowMin, and if they aren't the same then no lucky num
    let rowMinMax = Number.NEGATIVE_INFINITY;
    let colMaxMin = Number.POSITIVE_INFINITY;

    for(let row = 0; row < matrix.length; row ++) {
        const rowMin = Math.min(...matrix[row]);
        rowMinMax = Math.max(rowMin, rowMinMax);
    }

    for(let col = 0; col < matrix[0].length; col ++) {
        let colMax: number | undefined;
        for(let row = 0; row < matrix.length; row ++) {
            if(colMax === undefined) colMax = matrix[row][col];
            else {
                colMax = Math.max(colMax, matrix[row][col]);
            }
        }
        colMaxMin = Math.min(colMax, colMaxMin);
    }

    return colMaxMin === rowMinMax ? [colMaxMin] : [];
};