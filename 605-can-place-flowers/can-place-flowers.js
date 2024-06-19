/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    // What if no flowers to plant?
    if(n === 0) return true;
    // Iterate through flowerbed
    for(let i = 0; i < flowerbed.length; i++) {
    // If current value is 0, determine if previous value is 0 and next value is 0
        if(flowerbed[i] === 0) {
            if(
                (flowerbed[i - 1] === undefined || flowerbed[i - 1] === 0) && 
                (flowerbed[i + 1] === undefined || flowerbed[i + 1] === 0)
            ){
    // Decrement n and Skip ahead by 1
                n--;
                i++;
            }
        }
        if(n === 0) return true;
    }
    // return n === 0
    return n === 0;
};