function maxVowels(s: string, k: number): number {
// Define vowels array
    const vowels = ['a', 'e', 'i', 'o', 'u'];
// Use sliding window
// Define currVowelCount
    let currVowelCount = 0;
// Define maxVowelCount
    let maxVowelCount = Number.NEGATIVE_INFINITY;
// Define leftPointer
    let leftPointer = 0;
// Iterate through string 
    for(let i = 0; i < s.length; i++) {
    // If letter in vowels, add vowelCount
        if(vowels.includes(s[i])) {
            currVowelCount ++;
        }
    // If i - leftPointer + 1 = k  
        if(i - leftPointer + 1 === k) {
        // Determine maxVowelCount
            maxVowelCount = Math.max(currVowelCount, maxVowelCount);
        // If letter at leftPointer is vowel, decrement currVowelCount
            if(vowels.includes(s[leftPointer])) currVowelCount --; 
        // Move leftPointer
            leftPointer ++;
        }
    }
// Return maxVowelCount
    return maxVowelCount;
};