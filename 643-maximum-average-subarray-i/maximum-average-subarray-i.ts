function findMaxAverage(nums: number[], k: number): number {
// Use sliding window?
// Keep track of currSum, maxSum, and leftPointer
    let currSum = 0;
    let maxSum = Number.NEGATIVE_INFINITY;
    let leftPointer = 0;
    for(let i = 0; i < nums.length; i++) {
        currSum += nums[i];
        if (i - leftPointer + 1 === k) {
            maxSum = Math.max(currSum, maxSum);
            currSum -= nums[leftPointer];
            leftPointer ++;
        }
    }
// Return maxSum/k
    return maxSum/k;
};