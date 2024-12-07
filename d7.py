from itertools import product

def all_operators(n):
    items = ["+","*","||"]
    out = []
    for item in product(items, repeat=n):
        l = []
        for i in item:
            l.append(i)
        out.append(l)
    return out
    


def valid(value, line, all_op):
    #print(line)
    #print("value " + str(value))
    for i in range(len(all_op)):
        res = mul_with_op(line,all_op[i])
        #print("res " + str(res))
        if res == int(value):
            #print("true")
            return True
    return False

def mul_with_op(line, op):
    out = line[0]
    for i in range(len(op)):
        if op[i] == "+":
            out += line[i+1]
        elif op[i] == "*":
            out *= line[i+1]
        elif op[i] == "||":
            inter_out = str(out)
            inter_i = str(line[i+1])
            inter = inter_out+inter_i
            out = int(inter)

    return out



input = open("d7_input.txt","r")
lines = input.readlines()


output = 0

for line in lines:
    line = line.split(": ")
    print(line)
    value = line[0]
    equation = list(map(int,line[1].split(" ")))
    length = len(equation)
    operators = all_operators(length-1)
    res = valid(value, equation, operators)
    if res:
        output += int(value)

print(output)

