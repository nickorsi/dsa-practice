/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    if(nums.length < 3) return false;
// // // Could a sliding window be used? 
// // // Start a loop with a while loop inside
// //     console.log(nums.length);
// //     for(let i = 0; i < nums.length - 2; i++) {
// //         let left = i + 1;
// //         let right = i + 2;
// //         let nextSmallestAt;
// // // Run the while loop so long as left is less than length of nums - 1
// //         while(left < nums.length - 1) {
// //             if(nextSmallestAt === undefined && nums[left] < nums[i]) {
// //                 nextSmallestAt = left;
// //                 console.log('here', nextSmallestAt);
// //             }
// // // If value at left is greater than at i
// // // Else advance left
// //             console.log(i, left, right)
// //             if(nums[left] > nums[i]){
// // // If value at right is greater than left return true
// //                 if(nums[right] > nums[left]) {
// //                     return true;
// //                 } 
// //             } else {
// //                 left ++;
// //             }
// // // If right not at end advance right
// //             if(right !== nums.length) {
// //                 right ++;
// //             } else {
// //                 left ++;
// //                 right = left + 1;
// //             }   
// //         }

// //         if(nextSmallestAt) i = i - 1 + nextSmallestAt;
// //     }
// // // Return false if nothing returned
// //     return false;
// // Create a new array that tracks the value and position
//     const valuesAndIndexes = [];
//     for(let i = 0; i < nums.length; i++) {
//         valuesAndIndexes.push([nums[i], i]);
//     }
// // Sort the array by the value
//     valuesAndIndexes.sort((a, b) => a[0]-b[0]);
//     console.log(valuesAndIndexes);
//     for(let i = 0; i < nums.length - 2; i++) {
//     // Do a sliding window along this array to find progressively higher position values
//         let left = 1 + i;
//         let right = 2 + i;
//         let rightCount = 0;
//         let leftCount = 0;
//         let nextValue;
//         while(right < nums.length) {
//             console.log(i, left, right);
//             if(rightCount && leftCount) return true;
//             if(nextValue === undefined && valuesAndIndexes[left][0] > valuesAndIndexes[i][0]) {
//                 nextValue = left;
//             }
//             if(valuesAndIndexes[right][0] > valuesAndIndexes[left][0] && valuesAndIndexes[right][1] > valuesAndIndexes[left][1]) {
//                 if(!rightCount) rightCount++;
//             } else {
//                 right ++;
//                 rightCount = 0;
//             }
//             if(valuesAndIndexes[left][0] > valuesAndIndexes[i][0] && valuesAndIndexes[left][1] > valuesAndIndexes[i][1]) {
//                 if(!leftCount) leftCount++;
//             } else {
//                 left ++;
//                 leftCount = 0;
//             }
//         }
//         i = nextValue - 1;
//     }
// // Return true is the window lenght is 3
// // Return false otherwise
//     return false;

// Everything above either timed out or was wrong
// Keep track of two nubers, first and second
    let first;
    let second;
    for(let i = 0; i < nums.length; i++) {
// first is assigned to the first number AND every number after that is smaller than this
        console.log(first, second, nums[i])
        if(first === undefined || nums[i] < first) {
            first = nums[i];
        } 
// second is assigned to the first nuber larger than first and every number after that is smaller to second and larger than first
        else if((second === undefined || nums[i] < second) && nums[i] > first) {
            second = nums[i];
        } 
        if (second !== undefined && nums[i] > second) {
            return true;
        }
// Return true otherwise 
    }
// Return false otherwise
    return false;
}
