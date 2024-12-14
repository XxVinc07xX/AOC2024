import re

input = open("d14_input.txt")
lines = input.readlines()

map_x = 103
map_y = 101

def second_behavior(p,v,map_x,map_y,iter=0):
    if iter == 100:
        return (p[0],p[1])
    new_pos = ((p[0]+v[0])%map_x, (p[1]+v[1])%map_y)
    return second_behavior(new_pos,v,map_x,map_y,iter= iter+1)

final_pos = []

for line in lines:
    line = re.sub(r'^p=', '', line)
    line = re.sub(r'v=', '', line)
    line = line.split(" ")

    p = [int(num) for num in line[0].split(',')]
    p.reverse()
    v = [int(num) for num in line[1].split(',')]
    v.reverse()

    #print(p,v)

    final_pos.append(second_behavior(p,v,map_x,map_y))

final_pos.sort()

new_map = []
for i in range(map_x):
    new_map.append([0]*map_y)

for i in range(len(final_pos)):
    pos = final_pos[i]
    new_map[pos[0]][pos[1]] += 1

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(0,map_x//2):
    for j in range(0, map_y//2):
        q1 += new_map[i][j]

for i in range(0, map_x//2):
    for j in range(map_y//2+1, map_y):
        q2 += new_map[i][j]

for i in range(map_x//2 +1 , map_x):
    for j in range(0, map_y//2):
        q3 += new_map[i][j]

for i in range(map_x//2 +1, map_x):
    for j in range(map_y//2 +1, map_y):
        q4 += new_map[i][j]

print(q1* q2* q3* q4)

