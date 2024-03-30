function numSubarrayProductLessThanK(nums: number[], k: number): number {
    if (k === 0) return 0;

    let left: number = 0;
    let product: number = 1;
    let subarraySum: number = 0;

    for(let right = 0; right < nums.length; right++) {
        product *= nums[right];
        while (product >= k && left <= right) {
            product /= nums[left];
            left++;
        }
        if(product < k) {
            subarraySum += right - left + 1;
        }
    }
    return subarraySum;
};