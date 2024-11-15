function findSmallestSetOfVertices(n: number, edges: number[][]): number[] {
    // Graph problem, is this similar to finding the shortest path? If so, use bfs traversal
    // Need to create a map of node to edge relations
    // Can then traverse the map using a queue
    const edgeMap: Map<number, Array<number>> = new Map();

    for(const [node, edge] of edges) {
        if(edgeMap.has(node)) {
            const oldArray = edgeMap.get(node);
            edgeMap.set(node, [...oldArray, edge]);
        } else {
            edgeMap.set(node, [edge]);
        }
    }
    console.log(edgeMap);
    const queue: Array<number> = [];
    const seen: Set<number> = new Set();
    const minNodes: Set<number> = new Set();

    for(const [node, edges] of edgeMap) {
        if(!seen.has(node)) {
            queue.push(node); // Where to start bfs? Unsure this assumption is correct...
            seen.add(node);
            minNodes.add(node);

            while(queue.length > 0) {
                const currentNode: number = queue.shift();

                for(const edge of edgeMap.get(currentNode)) {
                    if(edgeMap.has(edge)) {
                        if(!seen.has(edge)) {
                            // console.log("edge= ", edge);
                            // console.log("seen= ", seen);
                            queue.push(edge);
                            seen.add(edge);
                        } else {
                            minNodes.delete(edge);
                        }
                    }
                }
            }
        }
    }
    return [...minNodes];
};

