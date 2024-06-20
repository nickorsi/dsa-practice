/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // CANT USE '/'
    // MUST BE o(n) runtime
    // Build prefix going left and suffix going right
    const preffix = new Array(nums.length).fill(1);
    const suffix = new Array(nums.length).fill(1);

    for(let i = 0; i < nums.length; i++) {
        if(nums[i-1] !== undefined) {
            preffix[i] = preffix[i-1] * nums[i-1];
        }
    }

    for(let i = nums.length - 1; i >= 0 ; i--) {
        if(nums[i+1] !== undefined) {
            suffix[i] = suffix[i+1] * nums[i+1];
        }
    }

    return preffix.map((el, i, arr) => {
        return el * suffix[i];
    })
};