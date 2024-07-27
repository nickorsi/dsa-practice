function equalPairs(grid: number[][]): number {
    // Can numbers be repeated? Can you have two of the same row numbers and only 1 columns number, so only 1 pair? 
    // Naive way, create every number possible in the row and col as the matrix is traversed
    // Store these in a rowNums and colNums array
    let pairCount = 0;
    const rowNumStrings: string[] = new Array(grid.length).fill('');
    const colNumStrings: string[] = new Array(grid.length).fill('');

    for(let row = 0; row < grid.length; row ++) {
        const rowNum: number[] = [];
        for(let col = 0; col < grid[0].length; col ++) {
            rowNumStrings[row] += `,${grid[row][col]}`;
            colNumStrings[col] += `,${grid[row][col]}`;
        }
    }
    // Create freq counter for both arrays
    const rowNumStringsCounter: Record<string, number> = {};
    const colNumStringsCounter: Record<string, number> = {};

    for(let i = 0; i < grid.length; i++) {
        if (rowNumStrings[i] in rowNumStringsCounter) {
            rowNumStringsCounter[rowNumStrings[i]] ++;
        } else {
            rowNumStringsCounter[rowNumStrings[i]] = 1;
        }
        if (colNumStrings[i] in colNumStringsCounter) {
            colNumStringsCounter[colNumStrings[i]] ++;
        } else {
            colNumStringsCounter[colNumStrings[i]] = 1;
        }
    }

    // Iterate through rowNums
    for(const rowNumString in rowNumStringsCounter) {
        // If in colNums, increment paircount and remove from colNums
        if(rowNumString in colNumStringsCounter) {
            pairCount += rowNumStringsCounter[rowNumString] * colNumStringsCounter[rowNumString];
        }
    }
    // Return pairCount
    return pairCount;
};