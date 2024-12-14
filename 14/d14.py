import re

input = open("d14_input.txt")
lines = input.readlines()

map_x = 103
map_y = 101

cur_pos = []

for line in lines:
    line = re.sub(r'^p=', '', line)
    line = re.sub(r'v=', '', line)
    line = line.split(" ")

    p = [int(num) for num in line[0].split(',')]
    p.reverse()
    v = [int(num) for num in line[1].split(',')]
    v.reverse()

    #print(p,v)
    cur_pos.append((p,v))

#print(cur_pos)
for test in range(1,1000000): #start at 1 bc idx 0 is the 1st second 
    breaked = False
    #print(test)
    new_list = []
    for pos in range(len(cur_pos)):
        item = cur_pos[pos]
        old_p = item[0]
        cur_v = item[1]
        new_p = ((old_p[0]+cur_v[0])%map_x, (old_p[1]+cur_v[1])%map_y)
        new_list.append((new_p,cur_v))
    cur_pos = new_list

    new_map = []
    for _ in range(map_x):
        new_map.append([0]*map_y)

    for i in range(len(cur_pos)):
        pos = cur_pos[i]
        new_map[pos[0][0]][pos[0][1]] += 1


    for i in range(map_x):
        for j in range(map_y):
            if new_map[i][j] > 1:
                breaked = True
                break
        if breaked:
            break

    if not breaked:
        print(test)
        break

