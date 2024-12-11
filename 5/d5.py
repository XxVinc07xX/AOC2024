file = open("d5_input.txt","r")
lines = file.readlines()

dict={}

for line in lines:
    if line == "\n":
        break
    line = line.split("|")
    if int(line[0]) not in dict.keys():
        dict[int(line[0])] = []
    dict[int(line[0])].append(int(line[1]))

list_idx = 0

for i in range(len(lines)):
    if lines[i] == "\n":
        list_idx = i

sum = 0

for i in range(list_idx+1, len(lines)):
    cur_line = lines[i]
    cur_line = cur_line.split(",")
    correct = 1
    for j in range(len(cur_line)):
        for k in range(j,len(cur_line)):
            if int(cur_line[k]) in dict.keys():
                if int(cur_line[j]) in dict[int(cur_line[k])]:
                    correct = 0
                    cur_line[j], cur_line[k] = cur_line[k], cur_line[j]
    if correct == 0:
        sum += int(cur_line[len(cur_line)//2])
    if correct == 1:
        #sum += int(cur_line[len(cur_line)//2])
        pass #PART1

print(sum)
