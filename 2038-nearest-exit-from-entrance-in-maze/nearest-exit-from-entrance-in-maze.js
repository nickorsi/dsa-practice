// /**
//  * @param {character[][]} maze
//  * @param {number[]} entrance
//  * @return {number}
//  */
// var nearestExit = function(maze, entrance) {
//     // Graph problem using bfs to find the shortest path
//     // Moves are up (-1,0), down (1,0), left (0,-1) and right (0,1)
//     // Valid moves are within the boundaries of the matrix AND not into a wall
//     // Exit is a empty cell on the perimeter of the matrix
//     const validMoves = [[-1,0], [1,0], [0,-1], [0,1]];
//     return traverseMaze(entrance, maze, validMoves);
// };

// function isExit(startX, startY, x, y, m, n) {
//     // console.log("exit check");
//     // console.log(x !== startX);
//     // console.log(y !== startY);
//     // console.log(x === 0);
//     // console.log(y === 0);
//     // console.log( x === n - 1);
//     // console.log( y === m - 1);
//     if( (x !== startX || y !== startY) &&
//         (x === 0 || 
//         y === m - 1 || 
//         y === 0 || 
//         x === n - 1)
//     ) return true;

//     return false;
// }

// function isValid(x, y, n, m, matrix) {
//     // console.log("valid check", x, y, n, m, matrix);
//     if(
//         (x >= 0 && x <= n - 1) && 
//         (y >= 0 && y <= m - 1) &&
//         matrix[y][x] === "."
//     ) return true;

//     return false;
// }

// function traverseMaze(position, matrix, validMoves) {
//     const y = position[0];
//     const x = position[1];
//     const m = matrix.length;
//     const n = matrix[0].length;
//     const queue = [[x, y, 0]];
//     const seen = new Set();
//     seen.add([y,x]);

//     while(queue.length > 0) {
//         const [currentX, currentY, currentMoves] = queue.shift();
//         // console.log("currentX= ", currentX);
//         // console.log("currentY= ", currentY);
//         // console.log("currentMoves= ", currentMoves);
//         // console.log("queue= ", queue);
//         if(isExit(x, y, currentX, currentY, m, n)) return currentMoves;

//         for(const [yValidMove, xValidMove] of validMoves) {
//             // console.log("xValidMove= ", xValidMove);
//             // console.log("yValidMove= ", yValidMove);
//             const newX = currentX + xValidMove;
//             const newY = currentY + yValidMove;

//             if(!seen.has([newX, newY]) && isValid(newX, newY, n, m, matrix)) {
//                 // console.log("isValid");
//                 seen.add([newX, newY]);
//                 queue.push([newX, newY, currentMoves + 1]);
//             }
//         }

//     }
//     return -1;
// }

const nearestExit = (maze, [y0, x0]) => {
    maze[y0][x0] = '@'
    const queue = [[y0, x0, 0]]
    while (queue.length) {
        const [y, x, step] = queue.shift()
        for (const [dy, dx] of [[-1, 0], [0, -1], [1, 0], [0, 1]]) {
            const ny = y + dy, nx = x + dx
            if (!maze[ny]?.[nx]) {
                if (step) return step
            } else if (maze[ny][nx] === '.') {
                queue.push([ny, nx, step + 1])
                maze[ny][nx] = '*'
            }
        }
    }
    return -1
}