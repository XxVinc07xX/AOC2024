input = open("d8_input.txt","r")
lines = input.read()
map = lines.split("\n")


def in_map(i,j,map):
    if i >= 0 and i <= len(map)-1 and j >= 0 and j <= len(map[0])-1:
        return True
    return False

def find_occurence(i,j,map):
    out = []
    value = map[i][j]
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x,y) != (i,j):
                if map[x][y] == value:
                    diff_i = abs(i-x)
                    diff_j = abs(j-y)
                    if i < x and j > y:
                        if in_map(i-diff_i, j+diff_j, map):
                            if (i-diff_i, j+diff_j) not in out:
                                out.append((i-diff_i, j+diff_j))
                        if in_map(x+diff_i, y-diff_j, map):
                            if (x+diff_i, y-diff_j) not in out:
                                out.append((x+diff_i, y-diff_j))

                    elif i < x and j < y:
                        if in_map(i-diff_i, j-diff_j, map):
                            if (i-diff_i, j-diff_j) not in out:
                                out.append((i-diff_i, j-diff_j))
                        if in_map(x+diff_i, y+diff_j, map):
                            if (x+diff_i, y+diff_j) not in out:
                                out.append((x+diff_i, y+diff_j))

                    elif i > x and j > y:
                        if in_map(i+diff_i, j+diff_j, map):
                            if (i+diff_i, j+diff_j) not in out:
                                out.append((i+diff_i, j+diff_j))
                        if in_map(x-diff_i, y-diff_j, map):
                            if (x-diff_i, y-diff_j) not in out:
                                out.append((x-diff_i, y-diff_j))

                    elif i > x and j < y:
                        if in_map(i+diff_i, j-diff_j, map):
                            if (i+diff_i, j-diff_j) not in out:
                                out.append((i+diff_i, j-diff_j))
                        if in_map(x-diff_i, y+diff_j, map):
                            if (x-diff_i, y+diff_j) not in out:
                                out.append((x-diff_i, y+diff_j))

                    elif i == x and j < y:
                        if in_map(i, j-diff_j, map):
                            if (i, j-diff_j) not in out:
                                out.append((i, j-diff_j))
                        if in_map(x, y+diff_j, map):
                            if (x, y+diff_j) not in out:
                                out.append((x, y+diff_j))

                    elif i == x and j > y:
                        if in_map(i, j+diff_j, map):
                            if (i, j+diff_j) not in out:
                                out.append((i, j+diff_j))
                        if in_map(x, y-diff_j, map):
                            if (x, y-diff_j) not in out:
                                out.append((x, y-diff_j))

                    elif i > x and j == y:
                        if in_map(i+diff_i, j, map):
                            if (i+diff_i, j) not in out:
                                out.append((i+diff_i, j))
                        if in_map(x-diff_i, y, map):
                            if (x-diff_i, y) not in out:
                                out.append((x-diff_i, y))

                    elif i < x and j == y:
                        if in_map(i-diff_i, j, map):
                            if (i-diff_i, j) not in out:
                                out.append((i-diff_i, j))
                        if in_map(x+diff_i, y, map):
                            if (x+diff_i, y) not in map:
                                out.append((x+diff_i, y))
    return out


marked = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] != "." and map[i][j] != "#":
            out = find_occurence(i,j,map)
            marked = list(set(marked)|set(out))

print(lines)
print(len(marked))

