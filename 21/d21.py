input = open("d21_input.txt")
lines = input.readlines()


numeric_pad = [['7','8','9'],
               ['4','5','6'],
               ['1','2','3'],
               ['/','0','A']]

dir_pad = [['/','^','A'],
           ['<','v','>']]


def find_symbol(path):
    out=""
    if len(path) == 1:
        out += 'A'
    else:
        for i in range(1,len(path)):
            if path[i-1][0] == path[i][0] and path[i-1][1] == path[i][1]+1: 
                out += '<'
            elif path[i-1][0] == path[i][0] and path[i-1][1] == path[i][1]-1:
                out += '>'
            elif path[i-1][0] == path[i][0]+1 and path[i-1][1] == path[i][1]:
                out += '^'
            elif path[i-1][0] == path[i][0]-1 and path[i-1][1] == path[i][1]:
                out += 'v'
    return out



def in_map(i,j,map):
    if i >= 0 and i <= len(map)-1 and j >= 0 and j <= len(map[0])-1:
        return True
    return False



def find_pos(char, numeric_pad):
    for i in range(len(numeric_pad)):
        for j in range(len(numeric_pad[0])):
            if numeric_pad[i][j] == char:
                return((i,j))

def bfs(start,end, map):
    q = []
    visited = []

    parent={}
    path_backward = []

    q.append(start)
    visited.append(start)

    while not len(q) == 0:
        cur = q.pop(0)
        cur_i = cur[0]
        cur_j = cur[1]

        if cur == end:
            #print(parent)
            path_backward.append(cur)
            #print("here")
            if len(parent) != 0:
                current = parent[cur]
                path_backward.append(current)
                while current != start:
                    current = parent[current]
                    path_backward.append(current)
            #print(path_backward)
            path_backward.reverse()
            return path_backward


        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for k in range(4):
            new_i = cur_i + directions[k][0]
            new_j = cur_j + directions[k][1]
            #print(new_i,new_j)

            if in_map(new_i, new_j, map) and not (new_i, new_j) in visited:
                #print(new_i,new_j)
                if map[new_i][new_j] != "/":
                    visited.append((new_i, new_j))
                    q.append((new_i, new_j))
                    parent[(new_i, new_j)] = cur

    return 0


sum = 0


for line in lines:
    init_pos = (3,2)
    print(line.strip())
    symbol_path = ""
    for char in line.strip():
        #print(char)
        char = find_pos(char, numeric_pad)
        path = bfs(init_pos,char,numeric_pad)
        init_pos = char
        #print("path",path)
        symbol = find_symbol(path)
        symbol_path += symbol
        symbol_path += 'A'
    print("symbol", symbol_path)

    init_pos_step2 = (0,2)
    symbol_path_step2 = ""
    for symbol in symbol_path:
        symbol = find_pos(symbol, dir_pad)
        path = bfs(init_pos_step2,symbol,dir_pad)
        #print("path", path)
        init_pos_step2 = symbol
        symbol_step2 = find_symbol(path)
        symbol_path_step2 += symbol_step2
        if len(path) > 1:
            symbol_path_step2 += 'A'
    print("symbol_step2", symbol_path_step2)

    init_pos_step3 = (0,2)
    symbol_path_step3 = ""
    for symbol in symbol_path_step2:
        symbol = find_pos(symbol, dir_pad)
        path = bfs(init_pos_step3,symbol,dir_pad)
        #print("path", path)
        init_pos_step3 = symbol
        symbol_step3 = find_symbol(path)
        symbol_path_step3 += symbol_step3
        if len(path) > 1:
            symbol_path_step3 += 'A'
    print("symbol_step3", symbol_path_step3)

    num_part = int(line.strip()[:-1])
    sum += num_part*len(symbol_path_step3)

print(sum)



