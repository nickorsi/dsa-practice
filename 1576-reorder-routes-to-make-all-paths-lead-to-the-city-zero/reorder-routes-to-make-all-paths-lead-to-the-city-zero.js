/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    // Given the edges of a unidirectional tree (no cycles)
    // Must traverse the tree and determine how many edges must be swapped so all paths lead to the root 0
    // Can create an map that stores cities to connections
    // Can then traverse the map 
    let swapEdgeCount = 0;
    const seenCities = new Set();
    const cityMap = createMap(connections);
    seenCities.add(0);
    _traverseCityMap(0, cityMap);
    return swapEdgeCount;

    function _traverseCityMap(city, cityMap) {
        for(const [newCity, direction] of cityMap.get(city)) {
            if(!seenCities.has(newCity)) {
                seenCities.add(newCity);
                if(direction == 1) swapEdgeCount ++;
                if(cityMap.has(newCity)) {
                    _traverseCityMap(newCity, cityMap);
                }
            }
        }
    }
}
/**
createMap function takes an array containing 2 element arrays [a,b] representing edges from a->b 
Returns a map with key of integers and value of array of arrays, where each subarray is 2 elements 
[a, b] where a is the connection to another integer and b denotes whether the edge direction was original (1) or not (0)
 */
function createMap(edges) {
    const map = new Map();
    for(const edge of edges) {
        // Set edge with given direction
        if(!map.has(edge[0])) {
            map.set(edge[0], [[edge[1], 1]]);
        } else {
            const existingEdges = map.get(edge[0]);
            existingEdges.push([edge[1], 1]);
            map.set(edge[0], existingEdges);
        }
        // Set edge for the opposite direction
        if(!map.has(edge[1])) {
            map.set(edge[1], [[edge[0], 0]]);
        } else {
            const existingEdges = map.get(edge[1]);
            existingEdges.push([edge[0], 0]);
            map.set(edge[1], existingEdges);
        }
    }
    return map;
}

