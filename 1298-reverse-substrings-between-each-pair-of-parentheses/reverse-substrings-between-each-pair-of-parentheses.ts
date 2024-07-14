// function reverseParentheses(s: string, rest: string = s, sArray: string[] = [], ans: string[] = [], parenCount = 0, firsClosedParenCount = true): string {
//     console.log('rest=', rest)
//     // If nothing left in rest,  return answer
//     if(rest === '') return ans.join('');
//     let currS: string[] = [];
//     // Else build up currS slicing off each letter from rest into currS
//     while(rest[0] !== '(' && rest[0] !== ')' && rest) {
//         currS.push(rest[0]);
//         rest = rest.slice(1);
//     }
//     // If first char in rest is "(" recurse passing in rest without first char and currS pushed into sArray
//     if(rest[0] === '(') {
//         console.log('Enter ( recursion')
//         if(parenCount > 0) {
//             sArray.push(currS.join(''));
//             console.log('sArray=', sArray);
//             return reverseParentheses(s, rest.slice(1), sArray, ans, parenCount + 1, true);
//         } else {
//             return currS.join('') + reverseParentheses(s, rest.slice(1), sArray, ans, parenCount + 1, true);
//         }
//     }
//     // If first char is ")"...
//     if(rest[0] === ')') {
//         console.log('Enter ) recursion')
//         // If ans is empty, fill it with the reverse version of currS
//         if(firsClosedParenCount) {
//             ans = [...currS.reverse()]
//         // Else, make answer the reversed verion of the last sArray element, the ans, and the currS combined
//         } else {
//             ans = [...sArray.pop().split(''), ...ans, ...currS].reverse();
//         }
//         // Recurse into the function passing in new rest and ans
//         console.log('sArray=', sArray, 'ans=', ans)
//         parenCount --;
//         if(parenCount === 0 && rest.slice(1).length > 1) {
//             console.log('here', rest.slice(1))
//             return ans.join('') + reverseParentheses(s, rest.slice(1), sArray, ans, parenCount, true)
//         } else {
//             return reverseParentheses(s, rest.slice(1), sArray, ans, parenCount, false)
//         }
//     }

//     return ans.join('') + currS.join('');
// };

// co
// etco
// octe
// edocteel
// leetcode

// Above was garbage
// function reverseParentheses(s: string): string {
//     let ans = '';
//     const stringStack: string[] = [];
//     let currS: string[] = [];
//     let parenCount = 0;
//     let firstCloseParen = true;

//     for(let i = 0 ; i < s.length; i ++) {
//         console.log(ans, currS, stringStack, parenCount);
//         if(s[i] !== '(' && s[i] !== ')') {
//             if(parenCount === 0) {
//                 ans += s[i];
//             } else {
//                 currS.push(s[i]);
//             }
//         } else if (s[i] === '(') {
//             if(parenCount > 0) {
//             // if(currS.length > 0) {
//                 stringStack.push(currS.join(''));
//             // }
//             }
//             parenCount ++;
//             currS = [];
//             firstCloseParen = true;
//         } else if (s[i] === ')') {
//             parenCount --; 
//             if(firstCloseParen) {
//                  currS.reverse();
//                  firstCloseParen = false;
//             } else {
//                 currS = [...stringStack.pop().split(''), ...currS].reverse();
//             }
//             if(parenCount === 0) {
//                 ans += currS.join('');
//                 currS = [];
//             }
//         }
//     }
//     return ans;
// }

function reverseParentheses(s: string): string {
    const stg_1:string[]=[];
    for(let i=0;i<s.length;i++){
        if(s[i]==")"){
            const stg_2:string[]=[];
            let lastElement:string=stg_1.pop();
            while(lastElement!="("){
                stg_2.push(lastElement);
                lastElement=stg_1.pop();
            }
            while(stg_2.length){
                stg_1.push(stg_2.shift());
            }
        }
        else{
            stg_1.push(s[i]);
        }
    }
    return stg_1.join("")
};