/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    // Use muliple pointers
    // Start with left at 0 and right at 1
    let left = 0;
    let right = 1;
    // Enter while loop and stop when...right is at the end? 
    while(right < nums.length) {
    // If left is 0 and right is nonzero, swap values and increment left
        if(nums[left] === 0 && nums[right] !== 0) {
            [nums[right], nums[left]] = [nums[left], nums[right]];
            left ++;
        } else if (nums[left] !== 0) {
            left ++;
        }
    // Increment right 
        right ++;
    }
};