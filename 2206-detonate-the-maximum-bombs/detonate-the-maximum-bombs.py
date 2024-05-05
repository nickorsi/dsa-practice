class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
# Create a hashmap recording neighbors for each bomb based on if hypotenuse distance from current bomb to neighbors bombs is within radius of the bomb
# Then use BFS to find the largest string of bombs based based on the neighbor sets
        bomb_hash = dict()
    
        for i in range(len(bombs)):
            start_x, start_y, start_r = bombs[i]
            if i < len(bombs):
                for j in range(i+1, len(bombs)):
                    end_x, end_y, end_r = bombs[j]
                    distance = math.sqrt(math.pow((start_x - end_x), 2) + math.pow((start_y - end_y), 2))
                    if start_r >= distance:
                        if i in bomb_hash:
                            bomb_hash[i].append(j)
                        else:
                            bomb_hash[i] = [j]
                    if end_r >= distance:
                        if j in bomb_hash:
                            bomb_hash[j].append(i)
                        else:
                            bomb_hash[j] = [i]
        print(bomb_hash)
        self.seen = set()
        self.curr_bomb_count = 1
        self.max_bomb_count = 1
     
            
        def dfs(bomb: int):
            for neighbor in bomb_hash[bomb]:
                if neighbor not in self.seen:
                    self.seen.add(neighbor)
                    self.curr_bomb_count += 1
                    if neighbor in bomb_hash:
                        dfs(neighbor)
                    
        for bomb in bomb_hash:
            self.seen = set()
            self.seen.add(bomb)
            self.curr_bomb_count = 1
            dfs(bomb)
            self.max_bomb_count = max(self.max_bomb_count, self.curr_bomb_count)
        return self.max_bomb_count
                