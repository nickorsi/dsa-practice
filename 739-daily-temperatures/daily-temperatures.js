/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
// Sliding window style problem
// Define days_to_warmer_temp as empty array
//     const days_to_warmer_temp = [];
// // Enter a loop to iterate through the temps
//     for(i = 0; i < temperatures.length; i++) {
//         let right_pointer = i + 1;
// // While right pointer is less than the length
//         while(right_pointer < temperatures.length) {
// // If temp at right is greater than ith temp, push into ans right pointer - i
//             if(temperatures[i] < temperatures[right_pointer]) {
//                 days_to_warmer_temp.push(right_pointer - i);
//                 right_pointer += temperatures.length;
//             }
// // Otherwise increment right pointer
//             right_pointer ++;
//         }
// // If ith value doesn't exist in ans, push 0
//         if(days_to_warmer_temp[i] === undefined) {
//             days_to_warmer_temp.push(0);
//         }
//     }
// // Return ans
//     return days_to_warmer_temp;

// Need to use a Monotonic stack
    const days = temperatures.length;
    const ans = new Array(days).fill(0);
    const stack = [];

    for(let i = 0; i < days; i++) {
        while(stack.length > 0 && temperatures[i] > stack[stack.length - 1][0]) {
            const [currTemp, currDays] = stack.pop();
            ans[currDays] = i - currDays;
        }
        stack.push([temperatures[i], i]);
    }

    return ans;
};