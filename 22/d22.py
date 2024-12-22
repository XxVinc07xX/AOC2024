input = open("d22_input.txt", "r")
lines = input.readlines()


def secret_behavior(number):
    step1_init = number*64
    step1_mix = step1_init ^ number
    step1_prune = step1_mix % 16777216

    step2_init = int(step1_prune // 32)
    step2_mix = step2_init ^ step1_prune
    step2_prune = step2_mix % 16777216

    step3_init = step2_prune * 2048
    step3_mix = step3_init ^ step2_prune
    step3_prune = step3_mix % 16777216

    return step3_prune


#PART1


sum = 0
overall_dic={}
last_4 = []


for line in lines:
    dic={}
    val = int(line)
    last_dig = str(val)[-1]
    for _ in range(2000):
        res = secret_behavior(val)
        last_dig_2 = str(res)[-1]
        diff = int(last_dig_2) - int(last_dig)
        last_4.append(diff)
        if len(last_4) == 4:
            tuple_last_4 = tuple(last_4)
            if not tuple_last_4 in dic.keys():
                dic[tuple_last_4] = 0
                dic[tuple_last_4] = int(last_dig_2)
            else:
                if int(last_dig_2) > dic[tuple_last_4]:
                    dic[tuple_last_4] = int(last_dig_2)
            last_4.pop(0)
        last_dig = last_dig_2
        val = res
    for key, value in dic.items():
        if not key in overall_dic:
            overall_dic[key] = value
        else:
            overall_dic[key] += value
    #print(val)
    sum += val


#PART2

seq = max(overall_dic, key=overall_dic.get) #get max value
#print(seq)
sum2=0



for line in lines:
    last_4 = []
    #print(line.strip())
    val = int(line)
    last_dig = str(val)[-1]
    for _ in range(2000):
        res = secret_behavior(val)
        last_dig_2 = str(res)[-1]
        diff = int(last_dig_2) - int(last_dig)
        last_4.append(diff)
        if len(last_4) == 4:
            tuple_last_4 = tuple(last_4)
            #print(tuple_last_4)
            if tuple_last_4 == seq:
                #print("eq seq", int(last_dig_2))
                sum2 += int(last_dig_2)
                break
            last_4.pop(0)
        last_dig = last_dig_2
        val = res

print(sum,sum2)


