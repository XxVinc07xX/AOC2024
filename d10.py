input = open("d10_input.txt", "r")
lines = input.read()
map = lines.split("\n")


def in_map(i,j,map):
    if i >= 0 and i <= len(map)-1 and j >= 0 and j <= len(map[0])-1:
        return True
    return False

def path(map,i,j):
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    score = 0
    q=[]
    visited = []
    q.append((i,j))
    while not len(q) == 0:
        idx = q.pop(0)
        value = map[idx[0]][idx[1]]
        visited.append((i,j))
        for k in range(4):
            x = idx[0]+direction[k][0]
            y = idx[1]+direction[k][1]

            if in_map(x, y, map) :
                if map[x][y] == str(int(value) +1):
                    if str(map[x][y]) == "9":
                        score += 1
                    else:
                        q.append((x,y))
    return score


                    




trailheads = []
score = 0

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "0":
            trailheads.append((i,j))
            score += path(map,i,j)

print(score)




