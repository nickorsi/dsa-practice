function largestAltitude(gain: number[]): number {
// Can use a prefix sum array, and can save space complexity using given array
// Iterate through gain
    for(let i = 0; i< gain.length; i ++) {
    // If at i === 0, continue 
        if(i === 0) continue;
    // Make current element in gain the sum of itself and the previous element
        gain[i] = gain[i] + gain[i-1];
    }
// Find maxAltitude in gain
    const maxAltitude = Math.max(...gain);
// If maxAltitude less than zero, return 0, else maxAltitude
    return maxAltitude < 0 ? 0 : maxAltitude;
};