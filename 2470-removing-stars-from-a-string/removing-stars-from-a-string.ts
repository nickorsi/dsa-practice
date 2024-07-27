function removeStars(s: string): string {
    // This looks recursive, will hold the answer going up and return it once no more letters exist UPDATE: may try a while loop
    let ans: string[] = [];
    if(!(s.includes('*'))) return s;

    for(let i = 0; i < s.length; i ++) {
        if (s[i] === '*' && i < s.length) {
            // console.log('here1', ans)
            while(s[i] === '*') {
                ans.pop();
                i ++;
            }
            i --;
        } else {
            // console.log('here2', ans)
            ans.push(s[i]);
        }
    }

    return ans.join('');
};