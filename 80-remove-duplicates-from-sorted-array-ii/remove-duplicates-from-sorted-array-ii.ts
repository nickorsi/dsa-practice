function removeDuplicates(nums: number[]): number {
    let left = 0;
    let right = 1;
    const indexOfSemiUniqueNums: number[] = [left];
    let counter = 1;

    while(right < nums.length) {
        if(nums[left] !== nums[right]) {
            indexOfSemiUniqueNums.push(right);
            left = right;
            counter = 1;
        } else if(counter < 2) {
            counter ++;
            indexOfSemiUniqueNums.push(right);
        }

        right ++;
    }

    for(let i = 1; i < indexOfSemiUniqueNums.length; i++) {
        if(i !== indexOfSemiUniqueNums[i]) {
            [nums[indexOfSemiUniqueNums[i]], nums[i]] = [nums[i], nums[indexOfSemiUniqueNums[i]]];
        }
    }
    
    return indexOfSemiUniqueNums.length;
};