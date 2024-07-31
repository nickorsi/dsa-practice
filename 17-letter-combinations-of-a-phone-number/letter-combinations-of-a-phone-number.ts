function letterCombinations(digits: string): string[] {
    // Define the hash map digitsToLetters
    const digitsToLetters = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'], 
        4: ['g', 'h', 'i'], 
        5: ['j', 'k', 'l'], 
        6: ['m', 'n', 'o'], 
        7: ['p', 'q', 'r', 's'], 
        8: ['t', 'u', 'v'], 
        9: ['w', 'x', 'y', 'z'], 
    }
    
    function _findLetterCombos(digits:string): string[] {
        if(digits.length === 0) return [];

        const letterCombos = digitsToLetters[digits[0]];

        const otherLetterCombos = _findLetterCombos(digits.slice(1));

        if (otherLetterCombos.length > 0) {
            const fullLetterCombos = [];
            
            for(const letterCombo of letterCombos) {
                for(const otherLetterCombo of otherLetterCombos) {
                    fullLetterCombos.push(letterCombo + otherLetterCombo);
                }
            }
            return fullLetterCombos;
        }
        return letterCombos;
    }

    return _findLetterCombos(digits);
};