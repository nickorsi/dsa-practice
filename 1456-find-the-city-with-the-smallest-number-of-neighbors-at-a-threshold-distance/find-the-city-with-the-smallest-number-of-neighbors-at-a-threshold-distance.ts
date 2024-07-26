function findTheCity(n: number, edges: number[][], distanceThreshold: number): number {
    // // Create a hash of all direct city relations WITH their weights, ensuring to track bi-directional relation
    // const cityHash: Record<string, number[][]> = {};

    // for(const edge of edges) {
    //     if (edge[0] in cityHash) {
    //         cityHash[String(edge[0])].push([edge[1], edge[2]]);
    //         cityHash[String(edge[0])].sort((a, b) => a[1] - b[1]);
    //     } else {
    //        cityHash[String(edge[0])] = [[edge[1], edge[2]]]; 
    //     }
    //     if (edge[1] in cityHash) {
    //         cityHash[String(edge[1])].push([edge[0],edge[2]]);
    //         cityHash[String(edge[1])].sort((a, b) => a[1] - b[1]);
    //     } else {
    //         cityHash[String(edge[1])] = [[edge[0],edge[2]]];
    //     }
    // }
    // // Must check for case where cities exist with no nodes, ie length of hashkeys is less than n
    // // If so iterate backwards from n and return first case where n doesn't exist in hash
    // if (Object.keys(cityHash).length < n) {
    //     for(let city = n - 1; city >= 0; city --) {
    //         if (!(city in cityHash)) return city;
    //     }
    // }
    // // console.log(cityHash);
    // let ansCity: number | undefined;
    // let minCities: number | undefined;
    // // Loop through the hash
    // for(const city in cityHash) {
    //     // console.log(ansCity, minCities);
    //     // On each loop, traverse through the relations returning an array of seen cities
    //     const traveledCities = cityTraversal(cityHash[city], 0, distanceThreshold, new Set([Number(city)]));
    //     // Put seen cities in a set 
    //     const traveledCitiesSet = new Set(traveledCities);
    //     // If length is less than minCities than replace it and replace city
    //     if (minCities === undefined || traveledCitiesSet.size < minCities) {
    //         minCities = traveledCitiesSet.size;
    //         ansCity = Number(city);
    //     // If same than take max value city
    //     } else if (traveledCitiesSet.size === minCities) {
    //         // console.log('here')
    //         ansCity = Math.max(ansCity, Number(city));
    //     }
    //     // console.log(ansCity, minCities);
    // }
    // // Return city
    // return ansCity;
    // // Define cityTraversal
    // function cityTraversal(cityEdges: number[][], distance: number = 0, distanceThreshold: number, citiesSeen: Set<number>): number[] {
    //     // console.log('cityTraversal', cityEdges, distance, distanceThreshold, citiesSeen);
    //     const citiesTraveled: number[] = [];
    //     for(const cityEdge of cityEdges) {
    //         // console.log('cityEdge', cityEdge, 'citiesSeen', citiesSeen);
    //         if (!(citiesSeen.has(cityEdge[0])) && distance + cityEdge[1] <= distanceThreshold ) {
    //             // citiesSeen.add(cityEdge[0])
    //             const newCitiesSeen = new Set([cityEdge[0], ...citiesSeen])
    //             const newDistance = distance + cityEdge[1]
    //             citiesTraveled.push(cityEdge[0], ...cityTraversal(cityHash[cityEdge[0]], newDistance, distanceThreshold, newCitiesSeen));
    //         }
    //     }
    //     return citiesTraveled;
    // }

// Above times out, below is from solutions
    function dijkstra(n: number, edges: number[][], start: number): number[] {
        const dist = Array(n).fill(Infinity);
        const nodeDist: { node: number; dist: number }[] = [];

        dist[start] = 0;
        nodeDist.push({ node: start, dist: 0 });

        while (nodeDist.length > 0) {
            //  console.log(dist, nodeDist)
            // Start with the node having the least distance
            nodeDist.sort((a, b) => a.dist - b.dist);
            const { node, dist: currDist } = nodeDist.shift()!;

            if (currDist > dist[node]) continue; // What is this? I guess it's skipping instances where the weighted distance to the node is greater than the distance already tracked to that node

            // Build the distances from the other citues
            for (const [from, to, weight] of edges) {
                // console.log(from, to, weight)
                if (from === node || to === node) { // Only care about nodes that are coming from or going to the current node
                    const neighbor = from === node ? to : from; // Assign the neighbor node accordingly
                    const newDist = currDist + weight; // Increase the CUMULATIVE WEIGHT ie DISTANCE
                    // console.log('neighbor', neighbor, 'newDist', newDist)
                    if (newDist < dist[neighbor]) {
                        dist[neighbor] = newDist;
                        nodeDist.push({ node: neighbor, dist: newDist });
                        // console.log('dist', dist, 'nodeDist', nodeDist)
                    }
                }
            }
        }

        return dist;
    }

  let minCity = -1;
  let minVisits = Infinity;

  for (let i = 0; i < n; i++) {
    const distances = dijkstra(n, edges, i);
    // console.log(distances)
    const visitsCount = distances.filter((d) => d <= distanceThreshold).length - 1; //Accounting for the city itself, -1

    if (visitsCount < minVisits || (visitsCount === minVisits && i > minCity)) {
      minCity = i;
      minVisits = visitsCount;
    }
  }

  return minCity;

};