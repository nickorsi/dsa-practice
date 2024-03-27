/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Can sort the array, which has O(n*logn) time complexity
    const sorted = nums.toSorted((a,b) => (a-b));
    // Once sorted can do two pointers to find if integers add up to target
    let left = 0;
    let right = nums.length-1;
    while(left < right) {
        // If equal
        if(sorted[left] + sorted[right] === target) {
        // Find index of first value
        //     const firstInd = nums.indexOf(sorted[left]);
        // // Find last index of second value
        //     const secondInd = nums.lastIndexOf(sorted[right]);
        // // Return array of indeces
        //     return [firstInd, secondInd];
            return [nums.indexOf(sorted[left]), nums.lastIndexOf(sorted[right])];
        }
        // If greater, move right down
        if(sorted[left] + sorted[right] > target) {
            right--;
            continue;
        }
        // If less, move left up
        else {
            left++;
            continue;
        }
    }
};