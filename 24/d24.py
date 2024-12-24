input = open("d24_input.txt", "r")
lines = input.readlines()

def behavior(line):
    if line[1] == "AND":
        res = int(dic[line[0]]) & int(dic[line[2]])
        dic[line[4]] = res
    elif line[1] == "OR":
        res = int(dic[line[0]]) | int(dic[line[2]])
        dic[line[4]] = res
    elif line[1] == "XOR":
        res = int(dic[line[0]]) ^ int(dic[line[2]])
        dic[line[4]] = res


dic={}

for line in lines[:90]:
    line = line.split(": ")
    dic[line[0]] = line[1].strip()

#print(dic)

todo=[]

for line in lines[91:]:
    line = line.split(" ")
    line[4] = line[4].strip()
    #print(line)
    if line[0] in dic and line[2] in dic:
        behavior(line)
    else:
        todo.append(line)

while not len(todo) == 0:
    line = todo.pop(0)
    line[4] = line[4].strip()
    if line[0] in dic and line[2] in dic:
        behavior(line)
    else:
        todo.append(line)

print(dic)

dic_keys = list(dic.keys())
dic_keys.sort()

sorted_dic = {i: dic[i] for i in dic_keys}
print(sorted_dic)

out=""
for key, value in reversed(sorted_dic.items()):
    if key[0] == 'z':
        out+=str(value)
    else:
        break

print(out)
print(int(out,2))
