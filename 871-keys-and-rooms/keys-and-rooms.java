class Solution {
    HashSet<Integer> seen = new HashSet<>();
    HashMap<Integer, List<Integer>> roomKeys;

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        // This is a graph traversal problem
        // If given n rooms, need to determine if traversal will hit n unique nodes
        // Given an array of edges, will make a hashmap of these relations
        this.roomKeys = buildHashMap(rooms);
        this.seen.add(0);
        // Will then traverse through these keeping track of seen rooms
        traverseRooms(this.roomKeys.get(0));
        // System.out.println(this.seen);
        // Return if hashset size is equal to rooms size
        return this.seen.size() == rooms.size();
    }

    public HashMap<Integer, List<Integer>> buildHashMap(List<List<Integer>> edges) {
        HashMap<Integer, List<Integer>> hashMap = new HashMap<>();
        for(int i = 0; i < edges.size(); i++) {
            hashMap.put(i, edges.get(i));
        }
        return hashMap;
    }

    public void traverseRooms(List<Integer> keys) {
        for(int key : keys) {
        // Only traverse to the room if it hasn't been seen yet
            if(!this.seen.contains(key)) {
        // Keep track of unique rooms seen in a hashset
                this.seen.add(key);
                List<Integer> newKeys = this.roomKeys.get(key);
                traverseRooms(newKeys);
            }
        }
    }
}