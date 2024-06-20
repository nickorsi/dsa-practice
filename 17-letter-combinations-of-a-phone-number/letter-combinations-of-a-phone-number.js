/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
  const numLetterHash = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r', 's'],
    '8': ['t','u','v'],
    '9': ['w','x','y', 'z'],
  }

  // const ans = [];

  // for(let i = 0; i < digits.length; i++) {
    
  // }

  function recurse(digits) {
    // Base case no numbers return empty array
    if(digits === '') {
      return [];
    }
    // If there's a digit, return the corresponding letters
    const ans = [];
    for(const letter of numLetterHash[digits[0]]) {
      const remainingLetter = recurse(digits.slice(1));
      if(remainingLetter.length > 0) {
        const letterCombos = remainingLetter.map((el, i, ar) => {
          return letter + el;
        })
        for(const letterCombo of letterCombos) {
          ans.push(letterCombo);
        }
      } else {
        ans.push(letter);
      }
      // ans.push(...letterCombos);
    }
    return ans;
  }

  return recurse(digits);
}