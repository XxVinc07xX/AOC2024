import re

input = open("d3_input.txt","r")
string = input.read()

#PART1

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", string)

sum = 0

for match in matches:
    match_dig = re.findall("\d{1,3}",match)
    dig1 = int(match_dig[0])
    dig2 = int(match_dig[1])
    sum += dig1 * dig2

#PART2

sum2 = 0

matches_part2 = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", string)

status = 1 #0 for don't(), 1 for do()

for i in range(len(matches_part2)):
    if matches_part2[i] == "do()":
        status = 1
    elif matches_part2[i] == "don't()":
        status = 0
    else:
        if status == 1:
            dig_inter = re.findall("\d{1,3}",matches_part2[i])
            dig21 = int(dig_inter[0])
            dig22 = int(dig_inter[1])
            sum2 += dig21*dig22

print(sum2)

