function isSubsequence(s: string, t: string): boolean {
    if(t.length < s.length) return false;
    if(t === s) return true;
    // Do two pointers
    let sPointer = 0;

    for(let i = 0; i < t.length; i ++) {
        // If the value of s @ sPointer and t @ i are the same increment sPointer
        if(s[sPointer] === t[i]) sPointer ++;
        // If sPointer > s.length return true
        if(sPointer >= s.length) return true;
    }
    // Return false
    return false;
    // Do recursion
};