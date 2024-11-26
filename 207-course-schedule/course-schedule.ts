function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // Graph style problem
    // Create a map of class requirements
    const courseMap: Map<number, Array<number>> = new Map();

    for(const [course, prereq] of prerequisites) {
        if(courseMap.has(course)) {
            const prereqs = courseMap.get(course);
            prereqs.push(prereq)
            courseMap.set(course, prereqs);
        } else {
            courseMap.set(course, [prereq]);
        }
    }
    console.log(courseMap);
    // Iterate through the the map
    const seenCourses: Set<number> = new Set();

    for(const [course, preqs] of courseMap) {

        if(!seenCourses.has(course)) {
            console.log("Start BFS, course= ", course)
            // seenCourses.add(course);
            if(!dfs(course, courseMap, seenCourses, new Set())) return false;
        }
    }
        // Then do dfs or bfs...will do bfs to find cycle quickly? Should have done dfs
        // Keep track of courses taken during bfs
    // Return coursesTaken === numCourses
    return true;
};

function bfs(course: number, courseMap: Map<number, Array<number>>, seenCourses: Set<number>, courseConflicts: Set<number>): boolean {
    const queue: Array<number> = [];
    queue.push(course)

    while(queue.length > 0) {
        const currentCourse = queue.shift();
        console.log("currentCourse= ", currentCourse);

        const prereqs = courseMap.get(currentCourse);

        for(const prereq of prereqs) {
            console.log("preq= ", prereq);
            console.log("courseConflicts= ", courseConflicts);
            if(courseConflicts.has(prereq)) {
                console.log("Here");
                return false;
            }
            courseConflicts.add(prereq)
            seenCourses.add(prereq);
            if(courseMap.has(prereq)) {
                queue.push(prereq);
            }

        }
    }
    return true;
}

function dfs(course: number, courseMap: Map<number, Array<number>>, seenCourses: Set<number>, courseConflicts: Set<number>) {
    console.log("course= ", course);
    if(!courseMap.has(course)) return true;
    if(courseConflicts.has(course)) return false;
    courseConflicts.add(course);

    for(const preq of courseMap.get(course)) {
        console.log("seenCourses= ", seenCourses);
        if(seenCourses.has(preq)) continue;
        const newCourseConflicts = new Set(courseConflicts)
        if(!dfs(preq, courseMap, seenCourses, newCourseConflicts)) {
            return false;
        }
        else {
            seenCourses.add(preq);
        }
    }
    return true;
}