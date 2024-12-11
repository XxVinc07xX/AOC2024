input = open("d11_input.txt","r")
line = input.readline()
line = line.split(" ")

def blink_behaviour(digit):
    inter = []
    if digit == "0":
        inter.append("1")
        return inter
    elif len(digit)%2 == 0:
        middle = len(digit)//2
        digit1 = digit[:middle]
        digit2 = digit[middle:]
        int_dig1 = int(digit1)
        digit1 = str(int_dig1) #remove extra 0
        int_dig2 = int(digit2)
        digit2 = str(int_dig2)
        inter.append(digit1)
        inter.append(digit2)
        return inter
    else:
        inter.append(str(int(digit)*2024))
        return inter
        
    

for i in range(25):
    new_line = []
    for j in range(len(line)):
        #print(line)
        res = blink_behaviour(line[j])
        if len(res) == 1:
            new_line.append(res[0])
        elif len(res) == 2:
            new_line.append(res[0])
            new_line.append(res[1])
    #print(new_line)
    line = new_line

print(len(line))