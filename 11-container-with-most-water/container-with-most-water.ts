function maxArea(height: number[]): number {
    // Naive way: Iterate through height
    // Keep track of the largest area
    let maxArea = 0;
    // for(let i = 0; i < height.length; i++) {
    // // On each iteration, while loop through the rest of nums
    //     let right = i + 1;

    //     while(right < height.length) {
    //         const minHeight = Math.min(height[i], height[right]);
    //         maxArea = Math.max(maxArea, minHeight * (right - i));
    //         right ++;
    //     }
    // }
    // // Return the area
    // return maxArea;

    // Two pointer way
    // Find max height? 
    // Start on either end
    let left = 0;
    let right = height.length -1 ;
    // Move points towards each other and calc water area at each point
    while(left < right) {
        const minHeight = Math.min(height[left], height[right]);
        maxArea = Math.max(maxArea, minHeight * (right - left));
    // Move the pointer with the short height value in
    // What to do on instances where the numbers are the same? Will try oving both in 
        if(height[right] === height[left]) {
            right --;
            left ++;
        } else if(height[right] > height[left]) {
            left ++;
        } else {
            right --;
        }
    }

    return maxArea;
};