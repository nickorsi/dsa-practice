/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {4
    const vowels = ['a','e','i','o','u'];
    const s_array = s.split('');
// Use multiple pointers and a while loop
    let leftPointer = s.length - 1;
    let rightPointer = 0;
    
    while(leftPointer >= rightPointer)  {
// Start on end, if both pointers are vowels swap
// If either isn't, advance that pointer
        if(vowels.includes(s_array[rightPointer].toLowerCase()) && vowels.includes(s_array[leftPointer].toLowerCase())) {
            [s_array[rightPointer], s_array[leftPointer]] = [s_array[leftPointer], s_array[rightPointer]];
            rightPointer++;
            leftPointer--;
        } else if(!(vowels.includes(s_array[rightPointer].toLowerCase()))) {
            rightPointer++;
        } else if(!(vowels.includes(s_array[leftPointer].toLowerCase()))) {
            leftPointer--;
        } else {
            rightPointer++;
            leftPointer--;
        }
        
    }
// Return the word
    return s_array.join('');
};