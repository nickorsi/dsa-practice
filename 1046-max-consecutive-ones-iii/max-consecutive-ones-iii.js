/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
//     Can contain k zeros in the array
//     Declare length = 0
    let currLength = 0;
//     Declare maxLength = currLength;
    let maxLength = currLength;
//     Declare windowStart = 0
    let windowStart = 0;
//     Decalre zeroCount = 0
    let zeroCount = 0;
//     For num of nums loop
    for(const num of nums) {
//      increment length
        currLength++;
//      if num = 0 increment zeroCount
        if (num === 0) zeroCount++;
//      while zeroCount > k
        while (zeroCount > k) {
//          if nums[windowStart] is 0, decrement zeroCount
            if (nums[windowStart] === 0) zeroCount--;
//          decrement length
            currLength--;
//          increment windowStart
            windowStart++;
        }
        maxLength = Math.max(maxLength, currLength);
    }
//     Return maxLength
    return maxLength;
};