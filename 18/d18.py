input = open("d18_input.txt", "r")
lines = input.readlines()

map_x = 71
map_y = 71
map=[]

#set map

for i in range(map_x):
    map.append(['.']*map_y)
    #print(map[i])

for line in lines:
    line = line.strip().split(",")
    line_i = int(line[1])
    line_j = int(line[0])
    #print(line_i, line_j)
    map[line_i][line_j] = "#"

#============

def in_map(i,j,map):
    if i >= 0 and i <= len(map)-1 and j >= 0 and j <= len(map[0])-1:
        return True
    return False

def path(start_i, start_j, end_i, end_j, map):

    parent = {}
    path_len = 0

    visited = []

    q = []
    q.append((start_i, start_j))
    visited.append((start_i, start_j))

    while not len(q) == 0:

        cur = q.pop(0)
        cur_i = cur[0]
        cur_j = cur[1]

        if (cur_i, cur_j) == (end_i, end_j):
            cur_back = parent[(cur_i,cur_j)]
            path_len += 1
            while (cur_back != (start_i,start_j)):
                cur_back = parent[cur_back]
                path_len += 1
            return path_len

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for k in range(4):
            new_i = cur_i + directions[k][0]
            new_j = cur_j + directions[k][1]

            if in_map(new_i, new_j, map) and (new_i, new_j) not in visited:
                if map[new_i][new_j] != "#":
                    visited.append((new_i,new_j))
                    q.append((new_i, new_j))
                    parent[(new_i,new_j)] = (cur_i, cur_j)

    return 0

print(path(0,0,70,70,map))



