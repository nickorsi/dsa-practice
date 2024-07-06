function longestSubarray(nums: number[]): number {
// If length of nums is 1, return 0
    if(nums.length === 1) return 0;
// Use sliding window keeping track of zeroCount, currLength, maxLength, and leftPointer
    let zeroCount = 0;
    let currLength = 0;
    let maxLength = 0;
    let leftPointer = 0;
// Iterate through nums
    for(let i = 0; i < nums.length; i ++) {
    // If nums at i is zero, increment zeroCount
        if(nums[i] === 0) zeroCount ++;
    // While zeroCount > 1
        while(zeroCount > 1) {
        // If nums[leftPointer] === 0 decrement zeroCount
            if(nums[leftPointer] === 0) zeroCount --;
        // Increment leftPointer
            leftPointer ++;
        }
    // Eval currLength and maxLength
        currLength = i - leftPointer + 1;
        maxLength = Math.max(maxLength, currLength);
    }
// If zeroCount === 0 return maxLength - 1 else return maxLength
    return maxLength - 1;
};