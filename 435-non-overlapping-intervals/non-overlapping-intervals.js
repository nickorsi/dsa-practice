/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    // let removalCount = 0;
    // intervals.sort((a, b) => {
    //     return (b[1] - b[0]) - (a[1] - a[0])
    // })
    // console.log(intervals)
    // for(let i = 0; i < intervals.length-1; i++) {
    //     for(let y = i+1; y < intervals.length; y++) {
    //         if(!(intervals[i][0] < intervals[y][0]) && !(intervals[i][0] >= intervals[y][1])) {
    //             removalCount ++;
    //             y = intervals.length
    //         }
    //     }
    // }

    // return removalCount;
    // intervals.sort((a, b) => (a[0] - b[0]));
    // const seen = new Set();
    // let skipped = 0;
    // let minSkipped = Number.POSITIVE_INFINITY;
    // console.log('intervals=', intervals)
    // for(let i = 0; i < intervals.length-1; i++) {
    //     console.log(intervals[i], seen, seen.has(intervals[i]))
    //     if(!(seen.has(intervals[i]))) {
    //         seen.add(intervals[i])
    //         let [start1, end1] = intervals[i];
    //         let rest_intervals = [...intervals.slice(0, i), ...intervals.slice(i+1)]
    //         console.log('rest_intervals=', rest_intervals, 'seen=', seen)
    //         for(let y = 0; y < rest_intervals.length; y++) {
    //             let [start2, end2] = rest_intervals[y];
    //             // console.log('start1=', start1, 'end1=', end1, 'start2=', start2, 'end2=', end2)
    //             if(start2 < start1 && end2 < start1) {
    //                 skipped++;
    //                 continue;
    //             }
    //             if(start2 >= end1) {
    //                 end1 = end2;
    //                 seen.add(rest_intervals[y])
    //                 continue;
    //             }
    //             skipped ++;
    //         }
    //         // console.log(skipped, minSkipped);
    //         minSkipped = Math.min(skipped, minSkipped);
    //         skipped = 0;
    //     }
    // }
    // return minSkipped === Number.POSITIVE_INFINITY ? 0 : minSkipped;

    intervals.sort((a, b) => (a[1] - b[1]))
    let ans = 0;
    let end = Number.NEGATIVE_INFINITY;

    for(let i = 0; i < intervals.length; i++) {
        const [currentStart, currentEnd] = intervals[i];

        if(currentStart >= end) {
            end = currentEnd;
        } else {
            console.log(end, currentStart, currentEnd)
            ans ++;
        }
        
    }

    return ans;
};