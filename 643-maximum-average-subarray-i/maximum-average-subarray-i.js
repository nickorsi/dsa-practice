/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
//     Declare currSum = 0
    let currSum = 0;
//     Loop through array of elements from 0 to less than k and add them to currSum
    for(let i = 0; i < k; i++) {
        currSum += nums[i];
    }
//     Declare right = 0
//     Declare left = k
//     Declare maxSum = currSum
    // let right = 0;
    let left = k;
    let maxSum = currSum;
//     While pointer less than/equal to length of nums
    while (left < nums.length) {
//      maxSum = max(maxSum, currSum-num[right]+num[left])
        currSum = currSum - nums[left-k] + nums[left]
        maxSum = Math.max(maxSum, currSum);
//      Increment right and left
        // right++;
        left++;
    }
//     Return maxSum/k
    return maxSum/k;
};