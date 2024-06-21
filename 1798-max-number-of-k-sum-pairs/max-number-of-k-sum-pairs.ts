function maxOperations(nums: number[], k: number): number {
// Use two pointers again? 
// Make a copy of the nums array
//     let numsCopy = [...nums];
// // Define left at 0 and right at 1
//     let left = 0;
//     let right = 1;
//     let pairs = 0;
// // While numsCopy has length greater than 1 and left less than numsCopy.length-1
//     while(numsCopy.length > 1 && left < numsCopy.length - 1) {
// //  If value at right and left add to k
//         // console.log(left, right);
//         if(numsCopy[left] + numsCopy[right] === k) {
//             // console.log('here');
// //      Move right value to in front of left value, then advance left by 2 and make right equal to left + 1
//             // numsCopy = [...numsCopy.slice(0, left), ...numsCopy.slice(left + 1, right), ...numsCopy.slice(right + 1)];
//             [numsCopy[left + 1], numsCopy[right]] = [numsCopy[right], numsCopy[left + 1]];
//             // console.log(numsCopy);
//             left += 2;
// //      Make right = left + 1
//             right = left + 1;
// //      Increment pairs
//             pairs ++;
// //  If right not at nums.length-1
//         } else if(right !== nums.length - 1) {
// //      Increment right
//             right ++;
// //  Else
//         } else {
// //      Increment left and make right = left + 1
//             left ++;
//             right = left + 1;
//         }
//     }
// // Return pairs
//     return pairs;
// Above times out
// Use a hash to count each value
// Iterate through hash and determine if it's pair exists
// If so decrement each value and add to count
    const numHash = {};
    let count = 0;
    for(const num of nums) {
        if(String(num) in numHash) {
            console.log('here');
            numHash[num] ++;
        } else {
            numHash[num] = 1;
        }
    }
    console.log(numHash);
    for(const key in numHash) {
        const numCount = numHash[key];
        const num = Number(key);
        const numPair = k - num;
        const numPairStr = String(numPair);

        if(numPairStr in numHash) {
            const numPairCount = numHash[numPairStr];
            const pairs = Math.min(numPairCount, numCount);

            if (numPair === num) {
                count += Math.floor(pairs/2);
                numHash[numPairStr] -= Math.floor(pairs/2);
            } else {
                count += pairs;
                numHash[numPairStr] -= pairs;
                numHash[key] -= pairs;
            }
        }
    }

    return count;
};
