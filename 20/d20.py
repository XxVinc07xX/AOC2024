from functools import cache
from collections import deque

input = open("d20_input.txt", "r")
lines = input.read()
map = lines.split("\n")

def in_map(i,j,map):
    if i >= 0 and i < len(map)-1 and j >= 0 and j < len(map[0])-1:
        return True
    return False


@cache
def bfs(map, start, end):
    q = deque()
    visited = set()

    parent = {}
    length = 0

    q.append(start)
    visited.add(start)

    while not len(q) == 0:
        cur = q.popleft()
        cur_i = cur[0]
        cur_j = cur[1]

        if cur == end:
            current = parent[cur]
            length += 1
            while current != start:
                current = parent[current]
                length += 1
            return length
        
        direction = [[0,1],[0,-1],[1,0],[-1,0]]

        for k in range(4):
            new_i = cur_i + direction[k][0]
            new_j = cur_j + direction[k][1]

            if in_map(new_i,new_j,map) and (new_i,new_j) not in visited:
                if map[new_i][new_j] != "#":
                    visited.add((new_i,new_j))
                    q.append((new_i,new_j))
                    parent[(new_i,new_j)] = cur

    return 0


start_pos = None
end_pos = None

original_length = 0
count = 0

map_tuple = tuple("".join(row) for row in map)
map = [list(row) for row in map]

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "S":
            start_pos = (i,j)
        elif map[i][j] == "E":
            end_pos = (i,j)

original_length = bfs(map_tuple,start_pos, end_pos)
print(original_length)

for i in range(1,len(map)-1):
    for j in range(1,len(map[0])-1):
        print(i,j)
        if map[i][j] == "#":
            map[i][j] = '.'
            map_tuple = tuple("".join(row) for row in map)
            var_length = bfs(map_tuple, start_pos, end_pos)
            if original_length - var_length >= 100:
                count += 1
            map[i][j] = "#"

print(count)




