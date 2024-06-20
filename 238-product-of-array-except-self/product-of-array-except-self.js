/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // CANT USE '/'
    // MUST BE o(n) runtime
    // Build prefix going left and suffix going right
    const ans = new Array(nums.length).fill(1);

    for(let i = 0; i < nums.length; i++) {
        if(nums[i-1] !== undefined) {
            ans[i] = ans[i-1] * nums[i-1];
        }
    }

    let accum = 1;

    for(let i = nums.length - 1; i >= 0 ; i--) {
        if(nums[i+1] !== undefined) {
            accum *= nums[i+1]
        }
            ans[i] = ans[i] * accum;
    }
    
    return ans
};