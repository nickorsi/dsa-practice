function passThePillow(n: number, time: number, person: number = 1, up: boolean = true): number {
// Use recursion or a stack going up AND THEN DOWN
// Want to include person as a parameter person: number starting at 1
// Base Case: time = 0 return person
    // console.log('time=', time, 'person=', person)
    if(time === 0) return person;
    time --;
// If person less than number or equal to 1 return recursion decrementing time and incrementing person
    if(person === 1) {
        up = true;
// If person equal to number return recursion decrementing time and decrementing person
    } 
    if(person === n) {
        up = false;
    }
    if(up){
        person++;
    } else {
        person--;
    }
    return passThePillow(n, time, person, up);
};