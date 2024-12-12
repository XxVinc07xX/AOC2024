import time

input = open("d12_input.txt")
lines = input.read()
map = lines.split("\n")

def in_map(i,j,map):
    if i >= 0 and i <= len(map)-1 and j >= 0 and j <= len(map[0])-1:
        return True
    return False

def check_neighbor(i, j, new_i, new_j, map):
    value = map[i][j]
    new_value = map[new_i][new_j]
    if value == new_value:
        return True
    return False

#print(check_neighbor(0,4,0,3,map))


already_visited = []

sum = 0

for i in range(len(map)):
    for j in range(len(map[0])):

        buffer = []

        if (i,j) not in already_visited:
            already_visited.append((i,j))
            buffer.append((i,j))


            area = 0
            perimeter = 0

            #print(buffer)


            while not len(buffer) == 0:
                #print(len(buffer))
                pos = buffer.pop(0)
                cur_i = pos[0]
                cur_j = pos[1]
                if (cur_i,cur_j) not in already_visited:
                    already_visited.append((cur_i,cur_j))
                area += 1
                value = map[cur_i][cur_j]

                direction = [[1,0],[-1,0],[0,1],[0,-1]]

                for k in range(4):
                    new_i = cur_i + direction[k][0]
                    new_j = cur_j + direction[k][1]

                    if in_map(new_i,new_j,map):
                        if check_neighbor(cur_i,cur_j,new_i,new_j,map) and (new_i,new_j) not in already_visited and (new_i,new_j) not in buffer:
                            buffer.append((new_i,new_j))
                            #print(buffer)
                            #time.sleep(1)
                        elif not check_neighbor(cur_i,cur_j,new_i,new_j,map):
                            perimeter += 1
                    else:
                        perimeter += 1
                    #print(k)
            #print(area, perimeter)

            sum += area*perimeter

print(sum)


