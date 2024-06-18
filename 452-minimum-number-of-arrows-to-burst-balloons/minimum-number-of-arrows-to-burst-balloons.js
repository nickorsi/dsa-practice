/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    points.sort((a, b) => (a[1] -b[1]));
    let darts = 0;
    let end = Number.NEGATIVE_INFINITY;

    for(let i = 0; i < points.length; i++) {
        const [currStart, currEnd] = points[i];
        if(currStart > end) {
            darts++;
            end = currEnd;
        }  
    }

    return darts;
};

// [[10,16],[2,8],[1,6],[7,12]] -> 2, [[10,16],[7,12]] overlaps @ 10, 11, 12 and [[2,8],[1,6]] overlaps @ 2, 3, 4, 5, 6
// Can a hash be created, and traveled through dfs or bfs
// points[0] overlaps with points[3]
// points[1] overlaps with points[2]
// points[2] overlaps with points[1]
// points[3] overlaps with points[0]
// But could have muliple layers of overlap, with some points hitting more balloons than others 
// Want to find the points that have the most ballons associated with them, then take those balloons out, and move to the next point with the most remaining balloos
// Sort the balloons by the starting value of the point with smallest balloons in front