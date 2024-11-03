class Solution {
    HashMap<Integer, int[]> cityConnections;
    HashSet<Integer> seenCities = new HashSet<>();
    int providenceCount = 0;

    public int findCircleNum(int[][] isConnected) {
        // This is another graph problem
        // Given a matrix of edge connections, these seem to be undirected edges? IE connection can be traversed from one node to another and back
        // Need to find the number of distinct trees in the graph, ie groups of nodes
        // Can create a hashMap of cityConnections
        // Can then traverse through each city in cityConnections and go through all the potential connections, only counting providences on the outter traversal
        this.cityConnections = createHashMap(isConnected);
        traverseProvidences(this.cityConnections);
        return this.providenceCount;
    }

    public HashMap<Integer, int[]> createHashMap(int[][] edgeMatrix) {
        HashMap<Integer, int[]> hashMap = new HashMap<>();

        for(int i = 0; i < edgeMatrix.length; i ++) {
            hashMap.put(i, edgeMatrix[i]);
        }

        return hashMap;
    }

    public void traverseProvidences(HashMap<Integer, int[]> cityConnections) {
        for(int city : cityConnections.keySet()) {
            if(!this.seenCities.contains(city)) {
                this.seenCities.add(city);
                this.providenceCount += 1;
                int[] connections = cityConnections.get(city);
                _traverseConnections(connections, cityConnections);
            }
        }
    }

    public void _traverseConnections( int[] connections, HashMap<Integer, int[]> cityConnections) {
        for(int i = 0; i < connections.length; i ++) {
            if(connections[i] == 1 && !this.seenCities.contains(i)) {
                this.seenCities.add(i);
                int[] newConnections = cityConnections.get(i);
                _traverseConnections(newConnections, cityConnections);
            }
        }
    }
}