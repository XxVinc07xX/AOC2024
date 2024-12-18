input = open("d4_input.txt","r")
lines = input.read()
map = lines.split("\n")

#for i
    #for j
        #if ij == x 
            #if in limits
                #check vertical
                #check horizontail
                #check diago
                #check backward


#===============================HELPER FUNCTIONS=================================

#PART1


def limits_hori(y,map):
    if y+3 <= len(map[0])-1:
        return True
    return False

def limits_back(y):
    if y-3 >= 0:
        return True
    return False

def limits_vert_down(x,map):
    if x+3 <= len(map)-1:
        return True
    return False

def limits_vert_up(x):
    if x-3 >= 0:
        return True
    return False

#nord_est
def limits_diag_ne(x,y,map):
    if y+3 <= len(map[0])-1 and x-3 >= 0:
        return True
    return False

#sud_est
def limits_diag_se(x,y,map):
    if y+3 <= len(map[0])-1 and x+3 <= len(map)-1:
        return True
    return False

#nord_ouest
def limits_diag_no(x,y):
    if y-3 >= 0 and x-3 >= 0:
        return True
    return False

#sud_ouest
def limits_diag_so(x,y,map):
    if y-3 >= 0 and x+3 <= len(map)-1:
        return True
    return False

def check_vert_down(i,j,map):
    if map[i+1][j] == "M" and map[i+2][j] == "A" and map[i+3][j] == "S":
        return True
    return False

def check_vert_up(i,j,map):
    if map[i-1][j] == "M" and map[i-2][j] == "A" and map[i-3][j] == "S":
        return True
    return False

def check_hori(i,j,map):
    if map[i][j+1] == "M" and map[i][j+2] == "A" and map[i][j+3] == "S":
        return True
    return False

def check_back(i,j,map):
    if map[i][j-1] == "M" and map[i][j-2] == "A" and map[i][j-3] == "S":
        return True
    return False

def check_diag_ne(i,j,map):
    if map[i-1][j+1] == "M" and map[i-2][j+2] == "A" and map[i-3][j+3] == "S":
        return True
    return False

def check_diag_se(i,j,map):
    if map[i+1][j+1] == "M" and map[i+2][j+2] == "A" and map[i+3][j+3] == "S":
        return True
    return False

def check_diag_no(i,j,map):
    if map[i-1][j-1] == "M" and map[i-2][j-2] == "A" and map[i-3][j-3] == "S":
        return True
    return False

def check_diag_so(i,j,map):
    if map[i+1][j-1] == "M" and map[i+2][j-2] == "A" and map[i+3][j-3] == "S":
        return True
    return False

#PART2 : check every possibility from pt of view of A

#M-S
#-A-
#M-S

def check_pattern(i,j,map):
    if map[i-1][j-1] == "M" and map[i-1][j+1] == "S" and map[i+1][j+1] == "S" and map[i+1][j-1] == "M":
        return True
    return False

#S-M
#-A-
#S-M

def check_pattern_back(i,j,map):
    if map[i-1][j-1] == "S" and map[i-1][j+1] == "M" and map[i+1][j+1] == "M" and map[i+1][j-1] == "S":
        return True
    return False


#M-M
#-A-
#S-S

def check_pattern_flip_down(i,j,map):
    if map[i-1][j-1] == "M" and map[i-1][j+1] == "M" and map[i+1][j+1] == "S" and map[i+1][j-1] == "S":
        return True
    return False


#S-S
#-A-
#M-M

def check_pattern_flip_up(i,j,map):
    if map[i-1][j-1] == "S" and map[i-1][j+1] == "S" and map[i+1][j+1] == "M" and map[i+1][j-1] == "M":
        return True
    return False


#===============================BODY=================================

#PART1 

sum = 0

for i in range(len(map)):
    for j in range(len(map[0])):
        #print((i,j))
        if map[i][j] == "X":
            if limits_hori(j,map):
                if check_hori(i,j,map):
                    sum += 1
            if limits_back(j):
                if check_back(i,j,map):
                    sum += 1
            if limits_vert_down(i,map):
                if check_vert_down(i,j,map):
                    sum += 1
            if limits_vert_up(i):
                if check_vert_up(i,j,map):
                    sum += 1
            if limits_diag_ne(i,j,map):
                if check_diag_ne(i,j,map):
                    sum += 1
            if limits_diag_se(i,j,map):
                if check_diag_se(i,j,map):
                    sum += 1
            if limits_diag_no(i,j):
                if check_diag_no(i,j,map):
                    sum += 1
            if limits_diag_so(i,j,map):
                if check_diag_so(i,j,map):
                    sum += 1

print(sum)

#PART2

sum_pt2 = 0


for i in range(1,len(map)-1):
    for j in range(1,len(map[0])-1):
        #print(map[i][j], (i,j))
        if map[i][j] == "A":
            if check_pattern(i,j,map):
                sum_pt2 += 1
            if check_pattern_flip_down(i,j,map):
                sum_pt2 += 1
            if check_pattern_flip_up(i,j,map):
                sum_pt2 += 1
            if check_pattern_back(i,j,map):
                sum_pt2 += 1

print(sum_pt2)
