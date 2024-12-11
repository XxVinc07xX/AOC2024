from functools import cache

input = open("d11_input.txt","r")
line = input.readline()
line = line.split(" ")

@cache
def blink_behaviour(digit, iter=0):
    if iter == 75: 
        return 1
    if digit == "0":
        return blink_behaviour("1", iter + 1) 
    elif len(digit) % 2 == 0: 
        middle = len(digit) // 2
        digit1 = str(int(digit[:middle]))  # Remove leading zeros
        digit2 = str(int(digit[middle:])) 
        return blink_behaviour(digit1, iter + 1) + blink_behaviour(digit2, iter + 1)
    else:  
        new_digit = str(int(digit) * 2024)
        return blink_behaviour(new_digit, iter + 1)
        
    

total_segments = 0
for dig in line:
    total_segments += blink_behaviour(dig)

print(total_segments)