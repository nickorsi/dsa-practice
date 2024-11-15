// function numWays(s: string): number {
// // First go through and count the number of 1's and 0's in the string
// // If the count of 1's is not a multiple of 3, then return 0
// // Otherwise believe there is a recursive method to continuously build the number of slices, with a condition checking that each slice has the same number of 1's
//     const onesAndZerosCount: Record<string, number> = {};

//     for(const char of s) {
//         if(char in onesAndZerosCount) {
//             onesAndZerosCount[char] ++;
//         } else {
//             onesAndZerosCount[char] = 1;
//         }
//     }
    
//     if("1" in onesAndZerosCount && onesAndZerosCount["1"] % 3 !== 0) return 0;
//     // Build the possible combinations of splits using the condtion of the amount of 1's required in each split
//     const onesRequired = "1" in onesAndZerosCount ? onesAndZerosCount["1"] / 3 : 0;
//     let splitVariationCount = 0;

//     function _buildSplits(s: string, condition: number, splits: Array<string>): void {
//         // console.log(splits);
//         let currentOneCount = 0;
        
//         if(splits.length === 2) {
//             if(s.length > 0) {
//                 for(const char of s) {
//                     if(char === "1") {
//                         currentOneCount ++;
//                     }
//                 }
//                 if(currentOneCount === condition) {
//                     // console.log("here");
//                     splitVariationCount ++;
//                 }
//             }
//             return
//         }
//         let currentString = '';

//         for(let i = 0; i < s.length; i ++) {
//             currentString += s[i];
//             if(s[i] === "1") {
//                 currentOneCount ++;
//             }
//             if(currentOneCount === condition) {
//                 const newSplits = [...splits, currentString];
//                 const newS = s.split("").slice(i+1).join("");
//                 _buildSplits(newS, condition, newSplits);
//             }
//             if(currentOneCount > condition) return;
//         }
//     }

//     _buildSplits(s, onesRequired, []);
//     return splitVariationCount;
// };
// Above Times Out at 159
function numWays(s: string): number {

    let arr_index_1 = []
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            arr_index_1.push(i)
        }
    }

    if (arr_index_1.length % 3 !== 0) return 0;
    if (arr_index_1.length == 0){
        let sum = 0;
        for (let i = 1; i < s.length-1; i++) {
            sum += i;
        }
        return sum % (10**9 + 7); 
    }

    const index = arr_index_1.length/3
    const a = arr_index_1[index] - arr_index_1[index-1]
    const b = arr_index_1[arr_index_1.length-index] - arr_index_1[arr_index_1.length-index-1]

    return (a * b) % (10**9 + 7)
};