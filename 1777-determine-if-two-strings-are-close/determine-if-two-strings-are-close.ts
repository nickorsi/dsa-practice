function closeStrings(word1: string, word2: string): boolean {
    // If lengths aren't the same, return false
    if(word1.length !== word2.length) return false;
    // Build frequency counter of the two strings, if they don't have the same count return false
    const freqCount1: Record<string, number> = {};
    const freqCount2: Record<string, number> = {};

    for(let i = 0; i < word1.length; i ++) {
        if(word1[i] in freqCount1) {
            freqCount1[word1[i]] ++;
        } 
        if(!(word1[i] in freqCount1)) {
            freqCount1[word1[i]] = 1;
        }
        if(word2[i] in freqCount2) {
            freqCount2[word2[i]] ++;
        }
        if(!(word2[i] in freqCount2)) {
            freqCount2[word2[i]] = 1;
        }
    }
    
    for(const key in freqCount1) {
        if(!(key in freqCount2)) return false;
    }

    const counts1 = Object.values(freqCount1).sort((a,b) => a-b);
    const counts2 = Object.values(freqCount2).sort((a,b) => a-b);

    for(let i = 0; i < counts1.length; i ++) {
        if(counts1[i] !== counts2[i]) {
            return false;
        }
    }

    return true;
};