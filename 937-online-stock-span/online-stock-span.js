
var StockSpanner = function() {
    this.stockSpans = [];
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    const length = this.stockSpans.length;
    let currSpan = 1;
    if(length > 0) {
        let [pastPrice, pastSpan] = this.stockSpans[length - 1];
        while(price >= pastPrice) {
            currSpan += pastSpan;
            if(this.stockSpans[length - currSpan] !== undefined){
                [pastPrice, pastSpan] = this.stockSpans[length - currSpan];
            } else {
                break;
            }
        }
    }

    this.stockSpans.push([price, currSpan]);

    return currSpan;
};

// price = 75
// stockSpans = [[100,1], [80,1], [60,1], [70,2], [60,1]]
// length = 5
// currSpan = 1
// pastPrice = 60
// pastSpan = 1
// 75 > 60 true
// currSpan = 2
// length - currSpan = 5 - 2 = 3 
// pastPrice = 70
// pastSpan = 2
// 75 > 60 false
// return 2

/** 
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */