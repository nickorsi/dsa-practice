function combinationSum3(k: number, n: number): number[][] {
    // Need to build combinations of size n using values 1-9
    // Need to be able to back track and ensure the sum is equal to k
    const combinations: number[][] = [];
    const validNums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

    function _findCombinations(k: number, n: number, combo: number[], validNums: number[]): void {
        // console.log("Ran findcombo");
        // console.log("k= ", k, "combo= ", combo, "validNums= ", validNums);
        if(k === 0) {
            const total = combo.reduce((accum, el, arr, i) => accum + el, 0)
            // console.log(combo, total);
            if(total === n) {
                combinations.push(combo);
            }
            return
        }
        for(let i = 0; i < validNums.length; i ++) {
            // console.log("Iteration i= ", i);
            const newCombo = [...combo, validNums[i]];
            const newValidNums = [...validNums.slice(i + 1)];
            const newK = k -1;

            _findCombinations(newK, n, newCombo, newValidNums);
            // console.log("here", "i= ", i, "validNums= ", validNums);
        }
        return
    }

    _findCombinations(k, n, [], validNums);
    return combinations;
};