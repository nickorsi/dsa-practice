function uniqueOccurrences(arr: number[]): boolean {
    // Build frequency counter
    const freqCounter: Record<string, number> = {};

    for(const num of arr) {
        if(String(num) in freqCounter) {
            freqCounter[String(num)] ++;
        } else {
            freqCounter[String(num)] = 1;
        }
    }
    // Iterate through counts

    const uniqueFreq: Set<number> = new Set();

    for(const freq of Object.values(freqCounter)) {
    // If in hash set return false
        if(uniqueFreq.has(freq)) return false;
    // Else add to hash set
        uniqueFreq.add(freq);
    }
    // Return true
    return true;
};