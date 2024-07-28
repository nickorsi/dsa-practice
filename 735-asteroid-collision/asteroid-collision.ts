function asteroidCollision(asteroids: number[]): number[] {
    const remainingAsteroids: number[] = [];
    // Naive approach, iterate through asteriods while building up ans
    for(let i = 0; i < asteroids.length; i ++) {
        // If empty, push into remaining asteroids
        if (remainingAsteroids.length === 0) {
            remainingAsteroids.push(asteroids[i]);
            continue;
        // Else if the previous asteroid is going right (> 0) and incoming asteroid going left (< 0)
        } else if (asteroids[i] < 0 && remainingAsteroids[remainingAsteroids.length-1] > 0) {
            // If absolute value of incoming asteroid is greater than previous asteroid, enter while loop
            if (Math.abs(asteroids[i]) > Math.abs(remainingAsteroids[remainingAsteroids.length-1])) {
                // While the previous asteroid moves right and incoming moves left, 
                // the incoming asteroid is larger than the previous asteroid, and there are previous asteroids, 
                // pop off the previous asteroid 
                while (
                    asteroids[i] < 0 && remainingAsteroids[remainingAsteroids.length-1] > 0 && 
                    Math.abs(asteroids[i]) > Math.abs(remainingAsteroids[remainingAsteroids.length-1]) &&
                    remainingAsteroids.length > 0
                ) {
                    remainingAsteroids.pop();
                }
                // If there are no remaining asteroids or the previous is moving left push on
                if (remainingAsteroids.length === 0 || remainingAsteroids[remainingAsteroids.length-1] < 0) {
                    remainingAsteroids.push(asteroids[i]);
                // If they are the same, popoff
                } else if (Math.abs(asteroids[i]) === Math.abs(remainingAsteroids[remainingAsteroids.length-1])) {
                    remainingAsteroids.pop();
                }
                // Else the previous asteroid is going right and is larger, and nothing is done
            // Else if they are equal they both explod and the previous asteroid must be popped off
            } else if (Math.abs(asteroids[i]) === Math.abs(remainingAsteroids[remainingAsteroids.length-1])) {
                remainingAsteroids.pop();
            // Else the incoming asteroid explodes and nothing happens
            }
        // Else the asteroids are either moving in the same direction or opposite directions, in which case the asteroid is added on
        } else {
            remainingAsteroids.push(asteroids[i]);
        }
    }
    return remainingAsteroids
};