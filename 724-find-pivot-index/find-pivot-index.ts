function pivotIndex(nums: number[]): number {
// Assign pivotIndex to -1
    let pivotIndex = -1;
// Create a prefix sum index from left to right (leftPrefix) and right to left (rightPrefix)
    const leftPrefix = new Array(nums.length).fill(0);
    const rightPrefix = new Array(nums.length).fill(0);
    for(let i = 0; i < nums.length; i ++) {
        if(i === 0 ) {
            leftPrefix[i] = nums[i];
            rightPrefix[nums.length - 1 - i] = nums[nums.length - 1 - i];
        } else {
            leftPrefix[i] = nums[i] + leftPrefix[i - 1];
            rightPrefix[nums.length - 1 - i] = nums[nums.length - 1 - i] + rightPrefix[nums.length - i];
        }
    }
    console.log(leftPrefix, rightPrefix);
// Iterate through leftPrefix 
    for(let i = 0; i < nums.length; i ++) {
    // If previous element of leftPrefix === next element of rightPrefix, assign index to pivotIndex
        if(i === 0 && rightPrefix[i + 1] === 0) {
            return i;
            console.log('here 1', pivotIndex);
        }
        else if(i === nums.length - 1 && leftPrefix[i - 1] === 0) {
            return i;
            console.log('here 2', pivotIndex);
        }
        else if(leftPrefix[i - 1] === rightPrefix[i + 1]) {
            return i;
            console.log('here 3', pivotIndex);
        }
    }
// Return pivotIndex
    return pivotIndex;
};