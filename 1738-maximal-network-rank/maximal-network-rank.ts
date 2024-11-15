function maximalNetworkRank(n: number, roads: number[][]): number {
    // Looking for pairs of cities that are directly connected AND have the most number of edges
    // Can create a map of the nodes to edges
    // Can then iterate through each node and look at each of the connected cities to see how many edges they have (minus 1)
    /**
        EX1:
        {
            0: [1, 3],
            1: [0, 2, 3],
            2: [1],
            3: [0, 1],
        }

        0 has 2 edges, it's pair 1 has 2 edges (taking out 0) and pair 3 has 1 edge (taking out 0) so 0-1 has 4 roads and 0-3 has 3 roads
        1 has 3 edges, it's pair 0 has 1 edge, it's pair 2 has 0 edges, and it's pair 3 has 1 edge, so still only 4 max
        2 has 1 edge and pair 1 has 2 edges
        3 has 2 edge and it's pair 0 has 1 and pair 1 has 2 has 2 edges sto still only 4 max
        Is there a way to stop this early? Will try naive approach first
     */ 
    
    const cityMap: Map<number, Set<number>> = new Map();

    for(const [city, road] of roads) {
        if(cityMap.has(city)) {
            cityMap.set(city, cityMap.get(city).add(road));
        } else {
            cityMap.set(city, new Set([road]));
        }
        if(cityMap.has(road)) {
            cityMap.set(road, cityMap.get(road).add(city));
        } else {
            cityMap.set(road, new Set([city]));
        }
    }
    
    // console.log(cityMap);

    let maxNetworkRank = 0;
    let iteration = 1;

    for(const [city, roads] of cityMap) {
        let currCityRank = roads.size;
        const cities = [...cityMap.keys()].slice(iteration);
        // console.log("city= ", city);
        // console.log("currCityRank= ", currCityRank);
        // console.log(cities);
        for(const nextCity of cities) {
            // console.log("nextCity= ", nextCity);
            const nextCityRoads = cityMap.get(nextCity)
            const nextCityRank = nextCityRoads.has(city) ? nextCityRoads.size - 1 : nextCityRoads.size;
            // console.log("nexCityRank= ", nextCityRank)
            maxNetworkRank = Math.max(maxNetworkRank, currCityRank + nextCityRank);
        }
        iteration ++;
    }

    return maxNetworkRank;
};