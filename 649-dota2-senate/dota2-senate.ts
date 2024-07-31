function predictPartyVictory(senate: string): string {
    // Option 1: Can a stack be used? 
    // const senateStack: string[] = [];
    // let votes = 0;
    // let rCount = 0;
    // let dCount = 0;
    // // Iterate through the seneate
    // for(const senator of senate) {
    //     // console.log(senator, rCount, dCount, senateStack)
    //     // If the stack is empty or the previous element is the same, push into stack and add to vote
    //     if (senateStack.length === 0 || senateStack[senateStack.length - 1] === senator) {
    //         // console.log('here 1')
    //         senator === "D" ? dCount ++ : rCount ++;
    //         senateStack.push(senator);
    //         votes ++;
    //     // Else the previous value is different and if they have votes, then decrement the vote and don't do anything else
    //     } else if (votes > 0) {
    //         // console.log('here 2')
    //         votes --;
    //     // Else they don't have votes and can pop one off add themselves, but not increment the vote
    //     } else {
    //         // console.log('here 3')
    //         if (senator === "D") {
    //             // console.log('here 4')
    //             dCount ++;
    //             rCount --;
    //         } else {
    //             // console.log('here 5')
    //             dCount --;
    //             rCount ++;
    //         }
    //         senateStack.pop();
    //         senateStack.push(senator)
    //     }
    // }
    // console.log(rCount, dCount, senateStack);
    // if (rCount === 0 || dCount === 0) {
    //     return dCount === 0 ? "Radiant" : "Dire";
    // }
    // if (rCount === 1 && rCount === dCount) {
    //     return senateStack[0] === "R" ? "Radiant" : "Dire";
    // }
    
    // return predictPartyVictory(senateStack.join(''));
    // Option 2: Can a counter be used? Order matters though
    // const senatorHash: Record<string, number> = {};

    // for(const senator of senate) {
    //     if (senator in senatorHash) {
    //         senatorHash[senator] ++;
    //     } else {
    //         senatorHash[senator] = 1;
    //     }
    // }
    // // Take into account only one or the other existing
    // if (!("D" in senatorHash)) return "Radiant";
    // if (!("R" in senatorHash)) return "Dire";
    // // If values aren't same, return  whoever has more people?
    // if (senatorHash["R"] !== senatorHash["D"]) {
    //     return senatorHash["R"] > senatorHash["D"] ? "Radiant" : "Dire";
    // // If the values are the same, return the first 
    // }
    // return senate[0] === "R" ? "Radiant" : "Dire"; 

    //Option 3: Neither of above work fully, looking at solution first is close but made easier using a QUEUE
    let rCount = 0;
    let dCount = 0;
    let rBanVotes = 0;
    let dBanVotes = 0;

    const q = [];

    for(const senator of senate) {
        if (senator === "D") {
            dCount ++;
        } else {
            rCount ++;
        }
        q.push(senator);
    }

    while(rCount > 0 && dCount > 0) {
        const currSenator = q.shift();

        if (currSenator === "D") {
            if (rBanVotes > 0) {
                rBanVotes --;
                dCount --;
            } else {
                dBanVotes ++;
                q.push(currSenator);
            }
        } else {
            if (dBanVotes > 0) {
                dBanVotes --;
                rCount --;
            } else {
                rBanVotes ++;
                q.push(currSenator);
            }
        }
    }

    return q[0] === "R" ? "Radiant" : "Dire";
};
