import heapq

input = open("d16_input.txt", "r")
lines = input.read()
map = lines.split("\n")

for line in map:
    print(line)

def in_map(i,j,map):
    if i >= 0 and i <= len(map)-1 and j >= 0 and j <= len(map[0])-1:
        return True
    return False

def valid_move(i,j,map):
    if in_map(i,j,map) and map[i][j] != "#":
        return True
    return False

def Dijkstra(map,starting_pos, end_pos):

    q=[]
    visited = []

    heapq.heappush(q, (0, starting_pos[0], starting_pos[1], (0,1)))

    costs = {(starting_pos[0], starting_pos[1]): [float('inf')] * 4}


    while not len(q) == 0:
        cur_cost, node_i, node_j, prev_dir = heapq.heappop(q)

        if (node_i, node_j) == end_pos:
            return cur_cost

        if (node_i, node_j, prev_dir) in visited:
            continue
        visited.append((node_i, node_j, prev_dir))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(4):
            new_i = node_i + directions[i][0]
            new_j = node_j + directions[i][1]

            if not valid_move(new_i, new_j, map):
                continue

            movement_cost = 1
            turn_cost = 0
            if prev_dir != i:
                turn_cost = 1000
            tot_cost = cur_cost + movement_cost + turn_cost

            if (new_i, new_j) not in costs:
                costs[new_i, new_j] = [float('inf')] * 4
            
            if tot_cost < costs[new_i,new_j][i]:
                costs[new_i, new_j][i] = tot_cost
                heapq.heappush(q, (tot_cost, new_i, new_j, i))

    return (float('inf'))


starting_pos = (len(map)-2, 1)
end_pos = (1, len(map[0])-2)

print(starting_pos, end_pos)

res = Dijkstra(map, starting_pos, end_pos)
print(res)

    