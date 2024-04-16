class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_coordinate = [0,0]
        visited_coordinates = {(0,0): 1}

        for char in path:
            if char == "N": curr_coordinate[0] += 1
            if char == "S": curr_coordinate[0] -= 1
            if char == "E": curr_coordinate[1] += 1
            if char == "W": curr_coordinate[1] -= 1

            if tuple(curr_coordinate) in visited_coordinates:
                return True
            else:
                visited_coordinates[tuple(curr_coordinate)] = 1
        
        return False