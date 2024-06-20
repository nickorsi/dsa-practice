/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // Split the string into an array, with splits targeted at spaces
    const splitS = s.split(' ');
    const ans = [];
    // Create an array containing all non-empty strings unshifted into the array
    for(const el of splitS) {
        if(el !== '') {
            ans.unshift(el);
        }
    }
    // Return the joined result with spaces in between
    return ans.join(' ');
};