function maxDepth(s: string): number {
    let maxDepth = 0;
    let currentDepth = 0;
    
    for(const char of s) {
        if(char === "(") {
            currentDepth ++;
        } else if (char === ")") {
            maxDepth = Math.max(maxDepth, currentDepth);
            currentDepth --;
        }
    }
    
    return maxDepth;
};
