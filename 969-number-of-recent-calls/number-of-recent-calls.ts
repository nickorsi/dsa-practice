class RecentCounter {
    set: Set<number>;

    constructor() {
        this.set = new Set();    
    }

    ping(t: number): number {
        this.set.add(t);
        // Don't need to loop through entire set, could do while loop
        for(const storedT of this.set) {
            if (storedT < t - 3000) {
                this.set.delete(storedT);
            }
        }
        return this.set.size;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */