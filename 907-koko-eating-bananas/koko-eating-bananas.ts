function minEatingSpeed(piles: number[], h: number): number {
    // Number of piles is always equal to or greater than h
    // So k will at most be the largest value in piles but could be as little as 1
    // Could start with k as the largest value and see if all the piles can be eaten in time
    // How to progress if. this doesn't work? could decrease by 1, but this will take forever. Could increase or decrease the rate by half the original rate
//     const maxPossibleRate = Math.max(...piles);
//     return binarySearchRate(piles, h, maxPossibleRate);
// };

// function binarySearchRate(piles: number[], h: number, k: number): number {
//     let totalTime = 0;

//     for(const pile of piles) {
//         totalTime += Math.ceil(pile / k);
//     }

//     if(totalTime === h) return k;
//     // If less than h, half the rate
//     const dK = Math.ceil(k / 2);
//     if(totalTime < h) {
//         // console.log(k, dK);
//         return binarySearchRate(piles, h, k - dK + 1);
//     }
//     return binarySearchRate(piles, h, k + dK - 1);
    // Above times out
    // Need a true binary search
    let right = Math.max(...piles);
    let left = 1;

    while(left < right) {
        const mid = Math.floor((left + right) / 2);
        let totalTime = 0;

        for(const pile of piles) {
            totalTime += Math.ceil(pile / mid);
        }

        if(totalTime <= h) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return right;
}
