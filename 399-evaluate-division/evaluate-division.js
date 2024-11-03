/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    // Need to relate each letter to a mathematical experssion
    // Everything in a relation with dividing, need to find when no variables are left after division
    // Try saving all variable combos in a nested map
    // First key represents the variable, and the associated value with be another map
    // This map will have all of the associated variable pairings and the resulting numerical value associated with that pair
    // Can then iterate through the queries
    // In each query, if either variable is not in the map then populate with -1
    // If the variables are the same then populate with 1
    // Otherwise, iterate through the potential pairings of the first variable and see if any of the pairs exist in the second variable pairings,
        // If so return the value
        // If not return -1
    // Return all of the query values
    const equationMap = createEquationMap(equations, values);
    // console.log("equationMap= ", equationMap);
    const queryAnswers = [];

    for(const [var1, var2] of queries) {
        if(!equationMap.has(var1) || !equationMap.has(var2)) {
            queryAnswers.push(-1);
        } else if(var1 == var2) {
            queryAnswers.push(1);
        } else {
            queryAnswers.push(findValue(var1, var2, equationMap));
        }
    }
    return queryAnswers;
};

function createEquationMap(equations, values) {
    const map = new Map();

    for(let i = 0; i < equations.length; i++) {
        const [var1, var2] = equations[i];
        const value = values[i];

        _insertIntoEquationMap(map, var1, var2, value);
        _insertIntoEquationMap(map, var2, var1, 1 / value);
    }

    function _insertIntoEquationMap(map, outterKey, nestedKey, value) {
        let varValueMap = new Map();
        if(map.has(outterKey)) {
            varValueMap = map.get(outterKey);
        }
        varValueMap.set(nestedKey, value);
        map.set(outterKey, varValueMap);
    }

    return map;
}

function findValue(var1, var2, equationMap) {
    const var1InnerMap = equationMap.get(var1);
    const var2InnerMap = equationMap.get(var2);
    // Check if there's a direct relation ie inverse of given equations
    if(var1InnerMap.has(var2)) return var1InnerMap.get(var2);
    // Otherwise traverse entire map to see if there is an indirect relation
    const seenVars = new Set([var1]);
    let totalValue = 1;
    let valueFound = false;
   _traverseRelations(equationMap, 1, var1InnerMap, var2);

    return valueFound ? totalValue : -1;

    function _traverseRelations(equationMap, currentTotalValue, relatingVars, targetVar) {
        // console.log(targetVar, relatingVars, totalValue);
        for(const [newVar, value] of relatingVars) {
            // console.log("newVar= ", newVar);
            if(newVar == targetVar) {
                totalValue = currentTotalValue * value;
                valueFound = true;
                return
            }
            if(!seenVars.has(newVar)) {
                seenVars.add(newVar); 
                newCurrentTotalValue = currentTotalValue * value;
                newRelatingVars = equationMap.get(newVar);
                _traverseRelations(equationMap, newCurrentTotalValue, newRelatingVars, targetVar);
            }
        }
    }
}