function decodeString(s: string): string {
    // This feels recursive in nature
    let decodedString = '';
    // Base case-ish is to when char === ']' return the current string
    // Iterate through s and build up decodedString
    for(let i = 0; i < s.length; i ++) {
        // If + char in an isNaN statement is FALSE
        // console.log(decodedString);
        if (!(isNaN(+ s[i]))) {
            // Save s[i] into repeatNum
            // Continue iterating i and adding to repeatNum until s[i] === '[]
            let repeatNumString = s[i];
            i ++;
            while (s[i] !== '[') {
                repeatNumString += s[i];
                i ++;
            }
            // Save result of recuring into decodeString passing in s.slice(i+2) as decodedPartialString
            // console.log('Enter Recursion', s.slice(i+2));
            const decodedPartialString = decodeString(s.slice(i +1 ));
            // Add into decodedString decodedPartialString.repeat(+char)
            decodedString += decodedPartialString.repeat(Number(repeatNumString));
            // console.log('Exit Recursion', 'decodedPartialString =', decodedPartialString, decodedString);
            // Need to iterate i until openCount matches closedCount
            let openCount = 1;
            let closedCount = 0;
            i += 1;
            while(openCount != closedCount) {
                i ++;
                if(s[i] === '[') openCount ++;
                if(s[i] === ']') closedCount ++;
            }
        // Else if char === ']' return decodedString
        } else if (s[i] === ']') {
            return decodedString;
        // Else add char into decodedString
        } else {
            decodedString += s[i];
        }
    }
    // Return decodedString
    return decodedString;
};