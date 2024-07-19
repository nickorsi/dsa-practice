function luckyNumbers (matrix: number[][]): number[] {
    // Define rowMins as an array m long with positive infintinty values and colMaxs n long with 0 values
    const rowMins = new Array(matrix.length).fill(Number.POSITIVE_INFINITY);
    const colMaxs = new Array(matrix[0].length).fill(0);
    // Iterate through matrix row and col
    for(let row = 0; row < matrix.length; row ++) {
        let rowMin = rowMins[row]
        for(let col = 0; col < matrix[0].length; col ++) {
        // If current value is smaller than value in rowMins at row, replace
            if(matrix[row][col] < rowMins[row]) rowMins[row] = matrix[row][col];
        // If current value is larger than value in colMaxs at col, replace
            if(matrix[row][col] > colMaxs[col]) colMaxs[col] = matrix[row][col];
        }
    }
    const luckyNums: number[] = [];
    // Iterate through rowMins
    for(const min of rowMins) {
    // If value in colMaxs, add to luckyNums array
        if(colMaxs.includes(min)) {
            luckyNums.push(min)
        }
    }
    // Return luckyNums
    return luckyNums;
};