from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
# Is a graph problem with an array of relations? Don't understand the relation between numCourses and prerequisites
# Can create a hash of the relations
# Can then traverse through the hash with a seen set
# If in seen, return false
        self.seen = set()
        self.course_hash = defaultdict(list)
        
        def bfs(course: int, path:set[int]) -> bool:
            if course in path:
                return False
            if course in self.seen:
                return True
            
            path.add(course)

            if course in self.course_hash:
                for req in self.course_hash[course]:
                    if not bfs(req, path):
                        return False
            
            path.remove(course)

            self.seen.add(course)

            return True

        for course, req in prerequisites:
            self.course_hash[course].append(req)

        self.course_hash = dict(self.course_hash)
    
        for course in self.course_hash:
            print(course)
            if not bfs(course, set()):
                return False
        
        return True