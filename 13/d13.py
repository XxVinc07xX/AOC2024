import re
from sympy import symbols, Eq, solve, core

input = open("d13_input.txt","r")
lines = input.readlines()

new_lines = []
for line in lines:
    if line != "\n":
        new_lines.append(line)
#print(new_lines)

def solve_eq_2_2_pt1(l1, l2, prize):
    x, y = symbols('x,y')
    eq1 = Eq((l1[0]*x + l2[0]*y), prize[0])
    eq2 = Eq((l1[1]*x + l2[1]*y), prize[1])
    res = solve((eq1,eq2), (x,y))
    if isinstance(res[x], core.numbers.Integer) and isinstance(res[y], core.numbers.Integer) and res[x] <= 100 and res[y] <= 100:
        return res[x], res[y]
    return None

def solve_eq_2_2_pt2(l1, l2, prize):
    x, y = symbols('x,y')
    eq1 = Eq((l1[0]*x + l2[0]*y), prize[0])
    eq2 = Eq((l1[1]*x + l2[1]*y), prize[1])
    res = solve((eq1,eq2), (x,y))
    if isinstance(res[x], core.numbers.Integer) and isinstance(res[y], core.numbers.Integer):
        return res[x], res[y]
    return None

sum1 = 0
sum2 = 0


for i in range(0,len(new_lines), 3):
    new_lines[i] = re.sub(r'^Button [A-Za-z]:\s*', '', new_lines[i])
    eq1 = re.findall(r'\d+', new_lines[i])
    eq1 = [int(num) for num in eq1]

    new_lines[i+1] = re.sub(r'^Button [A-Za-z]:\s*', '', new_lines[i+1])
    eq2 = re.findall(r'\d+', new_lines[i+1])
    eq2 = [int(num) for num in eq2]

    new_lines[i+2] = re.sub(r'^Prize:\s*', '', new_lines[i+2])
    prize = re.findall(r'\d+', new_lines[i+2])
    prize_pt1 = [int(num) for num in prize]
    prize_pt2 = [int(num) + 10000000000000 for num in prize]

    res1 = solve_eq_2_2_pt1(eq1,eq2,prize=prize_pt1)
    res2 = solve_eq_2_2_pt2(eq1,eq2,prize=prize_pt2)
    if res1:
        sum1 += 3*res1[0]
        sum1 += res1[1]

    if res2:
        sum2 += 3*res2[0]
        sum2 += res2[1]


print(sum1, sum2)