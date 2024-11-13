function tribonacci(n: number): number {
    // Tribonacci is the sum of the 3 previous trib numbers before the current number
    // T_0 = 0, T_1 = 1, T_2 = 1, T_3 = T_0 + T_1 + T_2 = 0+1+1 = 3, T_4 = T_1 + T_2 + T_3 = 1+1+2 = 4
    // Will rely on recursion with the following base cases
    // if(n === 0) return 0;
    // if(n === 1) return 1;
    // if(n === 2) return 1;
    // // Else return the sum of the past three recursions
    // return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1);
    // This times out though, is there a way to save the results in a dict?
    const memoizedTribs = new Map();
    memoizedTribs.set(0, 0);
    memoizedTribs.set(1, 1);
    memoizedTribs.set(2, 1);

    function _findTrib(n: number): number {
        if(memoizedTribs.has(n)) {
            return memoizedTribs.get(n);
        } else {
            memoizedTribs.set(n, _findTrib(n - 3) + _findTrib(n - 2) + _findTrib(n - 1));
        } 
        return memoizedTribs.get(n);
    }

    return _findTrib(n);
};