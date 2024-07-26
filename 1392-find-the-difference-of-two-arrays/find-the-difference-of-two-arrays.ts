function findDifference(nums1: number[], nums2: number[]): number[][] {
    const set1: Set<number> = new Set(nums1);
    const set2: Set<number> = new Set(nums2);
    
    for(const num of set1) {
        if(set2.has(num)) {
            set1.delete(num);
            set2.delete(num);
        }
    }

    return [[...set1], [...set2]];
};