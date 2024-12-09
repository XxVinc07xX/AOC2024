input = open("d9_input.txt","r")
line = input.readline()

def is_first_dig(l):
    last_dig = None
    for i in range(len(l)):
        if i == 0 and l[i] != ".":
            last_dig = i
        elif l[i] != ".":
            if last_dig != i-1:
                return False
            else:
                last_dig = i
    return True

def find_block_size(l,i):
    size = 0
    value = l[i]
    idx = i
    while(l[idx] == value and idx >= 0):
        size += 1
        idx -= 1
    return size

def find_space(l,n):
    for i in range(len(l)-n+1):
        found = True
        for j in range(n):
            if l[i+j] != ".":
                found = False
                break
        if found:
            return i
    return None






def first_missing(l):
    for i in range(len(l)):
        if l[i] == ".":
            return i    
    return None


idx_id = 0
l_first_out = []

for i in range(len(line)):
    if i%2 == 0:
        #first_out += int(line[i])*str(idx_id)
        for j in range(int(line[i])):
            l_first_out.append(str(idx_id))
        idx_id += 1
    elif i%2 != 0 and i != len(line)-1:
        #first_out += int(line[i])*"."
        for j in range(int(line[i])):
            l_first_out.append(".")

print("1 done")

#print(l_first_out)
#l_first_out = list(first_out)

#print(len(l_first_out), "len")
i = len(l_first_out)-1
while i>=0:
    if l_first_out[i] != ".":
        #print(i)
        #print(l_first_out[i])
        nb = find_block_size(l_first_out, i)
        space = find_space(l_first_out,nb)
        if space != None and space < i-nb:
            #print("free index for " + str(nb) + " blocs at index "+ str(space))
            #print(nb, space)
            for j in range(nb):
                l_first_out[space+j], l_first_out[i-j] = l_first_out[i-j], l_first_out[space+j]
        i -= nb
    else:
        i -= 1
    #print(l_first_out)

#print(l_first_out)




print("2 done") 
sum = 0
for i in range(len(l_first_out)):
    if l_first_out[i] != ".":
        sum += int(l_first_out[i])*(i)
print(sum)


