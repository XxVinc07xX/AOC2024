import time
input = open("d6_input.txt","r")
lines = input.read()
map = lines.split("\n")

def map_limit(position):
    if position[0] == 0:
        return True
    elif position[0] == len(map)-1:
        return True
    elif position[1] == 0:
        return True
    elif position[1] == len(map[0])-1:
        return True
    return False

def rotation(direction):
    if direction == "south":
        direction = "east"
    elif direction == "east":
        direction = "north"
    elif direction == "north":
        direction = "west"
    elif direction == "west":
        direction = "south"
    return direction


def exec_pt1():
    current_pos = (0,0)
    current_dir = "south"
    already_visited = []

    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] == "^"):
                #print(initial_position)
                already_visited.append((i,j))
                current_pos = ((i,j))

    while (not map_limit(current_pos)):
        #print(current_dir)
        #time.sleep(0.1)
        if current_dir == "south":
            if map[current_pos[0]-1][current_pos[1]] != "#":
                current_pos = (current_pos[0]-1, current_pos[1])
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited.append((current_pos[0], current_pos[1]))
            else:
                current_dir = rotation(current_dir)

        elif current_dir == "east":
            if map[current_pos[0]][current_pos[1]+1] != "#":
                current_pos = (current_pos[0], current_pos[1]+1)
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited.append((current_pos[0], current_pos[1]))
            else:
                current_dir = rotation(current_dir)

        elif current_dir == "north":
            if map[current_pos[0]+1][current_pos[1]] != "#":
                current_pos = (current_pos[0]+1, current_pos[1])
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited.append((current_pos[0], current_pos[1]))
            else:
                current_dir = rotation(current_dir)

        elif current_dir == "west":
            if map[current_pos[0]][current_pos[1]-1] != "#":
                current_pos = (current_pos[0], current_pos[1]-1)
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited.append((current_pos[0], current_pos[1]))
            else:
                current_dir = rotation(current_dir)

    print(len(already_visited))

def detect_loop(obstruction):
    #dict 
    #if already_visited with same direction return true
    #return false

    #print(obstruction)
    current_pos = (0,0)
    current_dir = "south"
    already_visited = {}

    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] == "^"):
                already_visited[(i,j)] = []
                already_visited[(i,j)].append("south")
                current_pos = ((i,j))

    #print(already_visited)

    while (not map_limit(current_pos)):
        #print(current_dir)
        #time.sleep(0.1)
        #print(already_visited)
        if current_dir == "south":
            if map[current_pos[0]-1][current_pos[1]] != "#" and (current_pos[0]-1,current_pos[1]) != obstruction:
                current_pos = (current_pos[0]-1, current_pos[1])
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited[(current_pos[0], current_pos[1])] = []
                    already_visited[(current_pos[0], current_pos[1])].append(current_dir)
                else:
                    if current_dir in already_visited[(current_pos[0], current_pos[1])]:
                        return False
                    else:
                        already_visited[(current_pos[0], current_pos[1])].append(current_dir)
            else:
                current_dir = rotation(current_dir)

        elif current_dir == "east":
            if map[current_pos[0]][current_pos[1]+1] != "#" and (current_pos[0],current_pos[1]+1) != obstruction:
                current_pos = (current_pos[0], current_pos[1]+1)
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited[(current_pos[0], current_pos[1])] = []
                    already_visited[(current_pos[0], current_pos[1])].append(current_dir)
                else:
                    if current_dir in already_visited[(current_pos[0], current_pos[1])]:
                        return False
                    else:
                        already_visited[(current_pos[0], current_pos[1])].append(current_dir)
            else:
                current_dir = rotation(current_dir)

        elif current_dir == "north":
            if map[current_pos[0]+1][current_pos[1]] != "#" and (current_pos[0]+1,current_pos[1]) != obstruction:
                current_pos = (current_pos[0]+1, current_pos[1])
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited[(current_pos[0], current_pos[1])] = []
                    already_visited[(current_pos[0], current_pos[1])].append(current_dir)
                else:
                    if current_dir in already_visited[(current_pos[0], current_pos[1])]:
                        return False
                    else:
                        already_visited[(current_pos[0], current_pos[1])].append(current_dir)
            else:
                current_dir = rotation(current_dir)

        elif current_dir == "west":
            if map[current_pos[0]][current_pos[1]-1] != "#" and (current_pos[0],current_pos[1]-1) != obstruction:
                current_pos = (current_pos[0], current_pos[1]-1)
                if (current_pos[0], current_pos[1]) not in already_visited:
                    already_visited[(current_pos[0], current_pos[1])] = []
                    already_visited[(current_pos[0], current_pos[1])].append(current_dir)
                else:
                    if current_dir in already_visited[(current_pos[0], current_pos[1])]:
                        return False
                    else:
                        already_visited[(current_pos[0], current_pos[1])].append(current_dir)
            else:
                current_dir = rotation(current_dir)

    return True




##debug

#PART1
#res = exec_pt1()

#PART2

nb_obs = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        print((i,j))
        if not detect_loop((i,j)):
            nb_obs += 1
print(nb_obs)



#for i in range(len(map)):
#    print(map[i])


