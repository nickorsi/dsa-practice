/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let mergedWord = '';
    for(let i = 0; i < word1.length; i++) {
        mergedWord += word1[i];
        if(word2[i] !== undefined) {
            mergedWord += word2[i];
        }
    }

    if(word2[word1.length] !== undefined) {
        mergedWord += word2.slice(word1.length);
    }

    return mergedWord;
};