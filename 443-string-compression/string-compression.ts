function compress(chars: string[]): number {
    // Define s as empty string
    let s = '';
    // Define count as 1
    let count = 0;
    // Iterate through chars
    for(let i = 0; i < chars.length; i++) {
    // If string is empty, push in char, and continue
        if(s === '') {
            s += chars[i];
            count ++;
        // } else if(i === chars.length - 1) {
        //     if(count >= 1) {
        //         count++;
        //         s += count;
        //         continue
        //     }
        //     s += chars[i];
        //     continue
    // If chars[i] not equal to the last string
        } else if(chars[i] !== s[s.length-1]) {
    //  If count is greater than 1
            if(count > 1) {
    //      push in count
                console.log('here', s);
                s += count;
                console.log(s);
            }
    //   push in letter
            s += chars[i];
    //   make count 1
            count = 1;
    // else increment count
        } else {
            console.log('here')
            count ++;
            if(i === chars.length -1) {
                s += count;
            }
        }
    } 
    // for(let i = 0; i < s.length; i++) {
    //     chars[i] = s[i];
    // }
    chars.splice(0, chars.length, ...s);

    return chars.length;
};