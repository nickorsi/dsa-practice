function minStartValue(nums: number[]): number {
// Track min value as preix is built
    let minVal: number = nums[0];
    const prefix: number[] = [nums[0]];
// Create prefix of the array
    for(let i = 1; i < nums.length; i++) {
        prefix[i] = prefix[i-1] + nums[i];
        minVal = Math.min(minVal, prefix[i]);
    }
// If in value >= 0 return 1 else return asb value of min
    return minVal >= 0 ? 1: Math.abs(minVal) + 1;
};