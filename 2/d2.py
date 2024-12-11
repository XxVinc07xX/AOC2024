input = open("d2_input.txt","r")
lines = input.readlines()

safe = 0

def safe_rm_inc(line):
    for i in range(1,len(line)):
        diff = line[i] - line[i-1]
        if diff < 1 or diff > 3:
            return False
    return True

def safe_rm_dec(line):
    for i in range(1,len(line)):
        diff = line[i-1] - line[i]
        if diff < 1 or diff > 3:
            return False
    return True

def can_be_safe(line):
    for i in range(len(line)):
        modified_line = line[:i] + line[i+1:]
        if safe_rm_inc(modified_line) or safe_rm_dec(modified_line):
            return True
    return False 

def init_safe_inc(line):
    for i in range(1,len(line)):
        #all inc
        if line[i] < line[i-1]:
            return False    
        #at most 3
        elif line[i] - line[i-1] > 3:
            return False 
        #at least 1
        elif line[i] - line[i-1] < 1:
            return False
    return True

def init_safe_dec(line):
    for i in range(1,len(line)):
        #all dec 
        if line[i] > line[i-1]:
            return False
        #at most 3
        elif line[i-1] - line[i] > 3:
            return False
        #at least 1
        elif line[i-1] - line[i] < 1:
            return False
    return True


safe_pt2 = 0

for line in lines:
    int_line = list(map(int,line.split()))
    #PART1
    if init_safe_inc(int_line) or init_safe_dec(int_line):
        safe_pt2 += 1
    #PART2
    elif can_be_safe(int_line):
        safe_pt2 += 1

print(safe_pt2)