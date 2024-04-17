class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_connections = {}
        city_count = len(isConnected)

        for city in range(city_count):
            city_connections[city] = []

            for connection in range(city_count):
                if city == connection: continue
                if isConnected[city][connection] == 1:
                    city_connections[city].append(connection)

        providence_count = 0
        interconnected_cities = set()

        for city in city_connections:
            if city in interconnected_cities: continue
            interconnected_cities.add(city)
            stack = [*city_connections[city]]
            while stack:
                curr_city = stack.pop()
                if curr_city in interconnected_cities: continue
                stack.extend(city_connections[curr_city])
                interconnected_cities.add(curr_city)

            providence_count += 1

        return providence_count
