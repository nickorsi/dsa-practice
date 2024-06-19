/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    // Find the larger of the two strings
    // Recursively find gdc
    // Then take this gdc value and dtermine if the letters from 0 to gdc repeat in both str1 and str2
    const maxLength = Math.max(str1.length, str2.length);
    const maxString = str1.length === maxLength ? str1 : str2;
    const minString = str1.length !== maxLength ? str1 : str2;

    function gdc(num1, num2) {
        if(num2 === 0) {
            return num1;
        }

        return gdc(num2, num1 % num2);
    }

    const gdc_num = gdc(maxString.length, minString.length);


    const stubMaxString = maxString.slice(0, gdc_num);
    const stubMinString = minString.slice(0, gdc_num);

    if(stubMaxString !== stubMinString) return '';

    let fullMaxString = '';
    let fullMinString = '';

    for(let i = 0; i < maxString.length / gdc_num; i ++) {
        fullMaxString += stubMaxString;
    }

    for(let i = 0; i < minString.length / gdc_num; i ++) {
        fullMinString += stubMinString;
    }

    if(fullMinString === minString && fullMaxString === maxString) {
        return stubMaxString;
    } else {
        return '';
    }
};