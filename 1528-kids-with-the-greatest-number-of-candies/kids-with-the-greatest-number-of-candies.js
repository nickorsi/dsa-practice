/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
// Determine what the current max value is in the set
// Use map to create a new array of booleans, where if the current value plus the extra is equal to or greater than current max, then true
    const currentMax = Math.max(...candies);

    return candies.map((el, ind, arr) => el + extraCandies >= currentMax);
};