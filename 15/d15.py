input = open("d15_input.txt")
lines = input.readlines()

def can_move(i,j,map,dir):
    if dir == "^":
        if dist_to_wall(i,j,map,dir) > nb_O(i,j,map,dir):
            return True
        return False
    elif dir == "v":
        if dist_to_wall(i,j,map,dir) > nb_O(i,j,map,dir):
            return True
        print(dist_to_wall(i,j,map,dir), nb_O(i,j,map,dir))
        return False
    elif dir == "<":
        if dist_to_wall(i,j,map,dir) > nb_O(i,j,map,dir):
            return True
        return False
    elif dir == ">":
        if dist_to_wall(i,j,map,dir) > nb_O(i,j,map,dir):
            return True
        return False

def move(i,j,map,dir):
    #print(map[i])
    map[i] = map[i][:j] + "." + map[i][j+1:]
    if dir == "^":
        if map[i-1][j] == "O":
            O_i,O_j = next_dot(i-1,j,map,dir)
            map[O_i] = map[O_i][:O_j] + "O" + map[O_i][O_j+1:]
        map[i-1] = map[i-1][:j] + "@" + map[i-1][j+1:]
        return (i-1,j)
    elif dir == "v":
        if map[i+1][j] == "O":
            O_i, O_j = next_dot(i+1,j,map,dir)
            map[O_i] = map[O_i][:O_j] + "O" + map[O_i][O_j+1:]
        map[i+1] = map[i+1][:j] + "@" + map[i+1][j+1:]
        return (i+1,j)
    elif dir == "<":
        if map[i][j-1] == "O":
            O_i, O_j = next_dot(i,j-1,map, dir)
            map[O_i] = map[O_i][:O_j] + "O" + map[O_i][O_j+1:]
        map[i] = map[i][:j-1] + "@" + map[i][j:]
        return (i,j-1)
    elif dir == ">":
        if map[i][j+1] == "O":
            O_i, O_j = next_dot(i, j+1, map, dir)
            map[O_i] = map[O_i][:O_j] + "O" + map[O_i][O_j+1:]
        map[i] = map[i][:j+1] + "@" + map[i][j+2:]
        return (i,j+1)
    

def dist_to_wall(i,j,map,dir):
    dist = 0
    if dir == "^":
        for k in range(i,0,-1):
            if map[k-1][j] == "#":
                return dist
            dist += 1
    elif dir == "v":
        for k in range(i,len(map)):
            if map[k+1][j] == "#":
                return dist
            dist += 1
    elif dir == "<":
        for k in range(j,0,-1):
            if map[i][k-1] == "#":
                return dist
            dist += 1
    elif dir == ">":
        for k in range(j,len(map[0])):
            if map[i][k+1] == "#":
                return dist
            dist += 1

def nb_O(i,j,map,dir):
    nb = 0
    if dir == "^":
        for k in range(i,0,-1):
            if map[k][j] == "#":
                return nb
            if map[k][j] == "O":
                nb += 1
    elif dir == "v":
        for k in range(i, len(map)):
            if map[k][j] == "#":
                return nb
            if map[k][j] == "O":
                nb += 1
    elif dir == "<":
        for k in range(j,0,-1):
            if map[i][k] == "#":
                return nb
            if map[i][k] == "O":
                nb += 1
    elif dir == ">":
        for k in range(j,len(map[0])):
            if map[i][k] == "#":
                return nb
            if map[i][k] == "O":
                nb += 1

    return nb

def next_dot(i,j,map,dir):
    if map[i][j] == ".":
            return [i,j]
    if dir == "^":
        for k in range(i,0, -1):
            if map[k-1][j] == '.':
                return [k-1,j]
    elif dir == "v":
        for k in range(i, len(map)):
            if map[k+1][j] == '.':
                return [k+1,j]
    elif dir == "<":
        for k in range(j,0,-1):
            if map[i][k-1] == '.':
                return [i,k-1]
    elif dir == ">":
        for k in range(j,len(map[0])):
            if map[i][k+1] == '.':
                return [i,k+1]
        


map = []
for i in range(50):
    map.append(lines[i].strip())


#print(map)

instr = ""
for i in range(51, len(lines)):
    instr += lines[i].strip() #skip \n

print(instr)



#DEBUG

for i in range(len(map)):
    print(map[i])


init_pos = (0,0)
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "@":
            init_pos = (i,j)
            

cur_pos = init_pos
for i in range(len(instr)):
    print(instr[i])
    if can_move(cur_pos[0],cur_pos[1],map,instr[i]):
        cur_pos = move(cur_pos[0], cur_pos[1], map, instr[i])
        #for j in range(len(map)):
            #print(map[j])

score = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "O":
            score += 100*i + j

print(score)
