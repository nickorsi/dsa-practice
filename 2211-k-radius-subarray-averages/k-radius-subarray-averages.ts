function getAverages(nums: number[], k: number): number[] {
//     If array length is less than 2*k, return an array made up of -1
    if (nums.length < 2*k+1) return Array(nums.length).fill(-1);
//     Generate a prefix array
    const prefix: number[] = [nums[0]];
//     Generate an answer array
    const answer: number[] = [];
    
    for(let i = 1; i < nums.length; i++) {
        prefix[i] = prefix[i-1] + nums[i];
    }
//     Loop through prefix and modify elements
    for(let i = 0; i < nums.length; i++) {
//      If i-k not truthy or i+k not truthy, answer[i] = -1
        if(prefix[i-k] === undefined || prefix[i+k] === undefined) answer[i] = -1;
//      Else make answer[i] = Floor value of value at prefix[i+k] - prefix[i-k] + nums[k] / 2 * K + 1
        else {
            answer[i] = Math.floor((prefix[i + k] - prefix[i - k] + nums[i - k]) / (2 * k + 1));
        }
    }
//     Return answer
    return answer;
};