input = open("d2_input.txt","r")
lines = input.readlines()

safe = 0

for line in lines:
    int_line = list(map(int,line.split()))
    order = 0 #0 for dec and 1 for inc
    init_first_value = int_line[0]
    init_sec_value = int_line[1]

    if init_first_value < init_sec_value:
        order = 1
        safe += 1
    elif init_first_value > init_sec_value:
        order = 0
        safe += 1
    else:
        order = 2


    #dec case
    if order == 0:
        for i in range(1,len(int_line)):
            #all inc 
            if int_line[i] >= int_line[i-1]:
                safe -= 1
                break
            #at most 3
            elif int_line[i-1] - int_line[i] > 3:
                safe -= 1
                break
            #at least 1
            elif int_line[i-1] - int_line[i] < 1:
                safe -= 1
                break


    #inc case
    if order == 1:
        for i in range(1,len(int_line)):
            #all inc
            if int_line[i] <= int_line[i-1]:
                safe -= 1
                break    
            #at most 3
            elif int_line[i] - int_line[i-1] > 3:
                safe -= 1
                break 
            #at least 1
            elif int_line[i] - int_line[i-1] < 1:
                safe -= 1
                break

           

print(safe)

        

    