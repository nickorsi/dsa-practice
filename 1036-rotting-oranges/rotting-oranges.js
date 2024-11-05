/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    // Graph problem, remember m is vertical (y) where 0 is top and m-1 is bottom, n is horizontal (x) where 0 is left and n-1 and right
    // console.log("grid=", grid);
    // console.log("grid[0][0]= ", grid[0][0]);
    const m = grid.length;
    const n = grid[0].length;
    const rottonOrangesQueue = [];
    const freshOranges = new Set();
    const seenOranges = new Set();
    // Find all orange (fresh & rootton) locations and save these
    for(let y = 0; y < m; y ++) {
        for(let x = 0; x < n; x ++) {
            if(grid[y][x] === 1) {
                freshOranges.add(`${y}${x}`);
            } else if(grid[y][x] === 2) {
                rottonOrangesQueue.push([y,x,0]);
                seenOranges.add(`${y}${x}`);
            }
        }
    }
    // If no rotten and no oranges, return 0 otherwise return -1
    if(rottonOrangesQueue.length == 0) {
        if(freshOranges.size === 0) return 0;
        return -1;
    } 
    // Otherwise need to progress through spredding the rot in 4 directions
    // Should do this in a queue setup to find the min number of minutes, keeping track of time on each round
    // console.log("rottonOrangesQueue= ", rottonOrangesQueue);
    // console.log("freshOranges= ", freshOranges);
    // console.log("seenOranges= ", seenOranges);
    // console.log("grid=", grid);
    // console.log("grid[0][0]= ", grid[0][0]);

    while(rottonOrangesQueue.length > 0) {
        // console.log("rottonOrangesQueue= ", rottonOrangesQueue);
        // console.log("freshOranges= ", freshOranges);
        // console.log("seenOranges= ", seenOranges);
        const [y, x, time] = rottonOrangesQueue.shift();
        // If there aren't any more rotton oranges and no more freshOranges, return time
        if(rottonOrangesQueue.length === 0 && freshOranges.size ===0) return time;
        // Go through possible moves...
        for(const [dY, dX] of [[-1,0],[1,0],[0,-1],[0,1]]) {
            const nY = y + dY;
            const nX = x + dX;
            // If...
            // console.log("nY= ", nY, "nX= ", nX);
            // console.log(typeof nY);
            // console.log(typeof nX);
            // console.log("grid[nY][nX]= ", grid[dY][dX]);
            if(
                // It's in the matrix
                (nY >= 0 && nY < m) && (nX >= 0 && nX < n) &&
                // It's a fresh orange
                grid[nY][nX] === 1 &&
                // It hasn't been see
                !seenOranges.has(`${nY}${nX}`)
            ) {
                // Then remove from freshOranges, add to seen, and add to queue
                freshOranges.delete(`${nY}${nX}`);
                seenOranges.add(`${nY}${nX}`);
                rottonOrangesQueue.push([nY, nX, time + 1]);
            }
        }
    }
    // Else return -1
    return -1;
};