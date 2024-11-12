class SmallestInfiniteSet {
    // Need to keep track of popped numbers
    poppedNums: Set<number>;
    addedNums: Set<number>;
    constructor() {
        this.poppedNums = new Set();
        this.addedNums = new Set();
    }

    popSmallest(): number {
        if(this.addedNums.size === 0) {
            if(this.poppedNums.size === 0) {
                this.poppedNums.add(1);
                return 1;
            } else {
                const poppedNumsList = [...this.poppedNums];
                poppedNumsList.sort((a,b) => a - b);
                const newNum = poppedNumsList[poppedNumsList.length - 1] + 1;
                this.poppedNums.add(newNum);
                return newNum;
            }
        } else {
            const addedNumsList = [...this.addedNums];
            addedNumsList.sort((a,b) => a - b);
            const newNum = addedNumsList[0];
            this.addedNums.delete(newNum);
            return newNum;
        }
    }

    addBack(num: number): void {
        if(this.poppedNums.has(num)) {
            this.addedNums.add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * var obj = new SmallestInfiniteSet()
 * var param_1 = obj.popSmallest()
 * obj.addBack(num)
 */