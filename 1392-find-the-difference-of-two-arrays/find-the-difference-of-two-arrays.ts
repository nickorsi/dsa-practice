function findDifference(nums1: number[], nums2: number[]): number[][] {
    let ans: number[][] = [[],[]];
    // Create hash set of nums1 and nums2
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    // Iterate through set1
    for(const uniqueNum of set1) {
        // If not in set2, push into ans[0]
        if(!set2.has(uniqueNum)) {
            ans[0].push(uniqueNum);
        }
        // Else remove from set2
        else {
            set2.delete(uniqueNum);
        }
    }
    // Assign ans[1] to spread out array of set2
    ans[1] = [...set2];
    // Return ans  
    return ans;

};