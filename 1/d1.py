input = open("d1_input.txt", "r")

col1=[]
col2=[]

lines = input.readlines()

for line in lines:
    line = line.split(" ")
    col1.append(int(line[0]))
    col2.append(int(line[3]))

#PART1

col1.sort()
col2.sort()

totDist = 0

for i in range(len(col1)):
    totDist += abs(col1[i] - col2[i])

print(totDist)

#PART2

similarity_score = 0

for value in col1:
    count = col2.count(value)
    similarity_score += count * value

print(similarity_score)


