function longestOnes(nums: number[], k: number): number {
// Sldiing window, find the max length including k zero's
// Keep track of zeroCount
    let zeroCount = 0;
// Have a leftPointer
    let leftPointer = 0;
// Keep track of currLength
    let currLength = 0;
// Keep track of maxLength
    let maxLength = Number.NEGATIVE_INFINITY;
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] === 0) zeroCount ++;
// While zeroCount > k, move leftPointer until less than = k, adjusting currLength
        while(zeroCount > k) {
            if(nums[leftPointer] ===0) zeroCount--;
            leftPointer ++;
        }
// Eval currLength and maxLength
        currLength = i - leftPointer + 1;
        maxLength = Math.max(currLength, maxLength);
    }
// Return maxLength
    return maxLength;
};