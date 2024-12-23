input = open("d23_input.txt")
lines = input.readlines()

def check(list1, list2, dic, key):
    if list1[0] == key:
        non_list1_key = list1[1]
    else:
        non_list1_key = list1[0]
    if list2[0] == key:
        non_list2_key = list2[1]
    else:
        non_list2_key = list2[0]
    if (non_list1_key, non_list2_key) in dic[non_list1_key] or (non_list2_key, non_list1_key) in dic[non_list1_key]:
        return True
    return False

def present_in_triple(lst, tpl):
    tuple_1 = tpl[0]
    tuple_2 = tpl[1]
    tuple_3 = tpl[2]
    if (tuple_1, tuple_2, tuple_3) in lst or (tuple_1, tuple_3, tuple_2) in lst or (tuple_3, tuple_2, tuple_1) in lst or (tuple_2, tuple_1, tuple_3) in lst or (tuple_2, tuple_3, tuple_1) in lst or  (tuple_3, tuple_1, tuple_2) in lst:
        return True
    return False

def count_t(lst):
    out = 0
    for  i in range(len(lst)):
        if lst[i][0][0] == 't' or lst[i][1][0] == 't' or lst[i][2][0] == 't':
            out += 1
    return out




dic={}

for line in lines:
    #print(line)
    line = line.split("-")
    line[1] = line[1].strip()
    tuple_line = (line[0], line[1])
    #print(tuple_line)
    if line[0] not in dic:
        dic[line[0]] = []

    if line[1] not in dic:
        dic[line[1]] = []
    
    if (line[0], line[1]) not in dic[line[0]] or (line[1], line[0]) not in dic[line[0]]:
        dic[line[0]].append(tuple_line)
    
    if  (line[0], line[1]) not in dic[line[1]] or (line[1], line[0]) not in dic[line[1]]:
        dic[line[1]].append(tuple_line)

#print(dic)

triple = []

for key, value in dic.items():
    print(key)
    if len(value) >= 2:
        for i in range(len(value)):
            for j in range(len(value)):
                if i != j:
                    if check(value[i], value[j], dic, key):
                        if value[i][0] == key:
                            new_val1 = value[i][1]
                        else:
                            new_val1 = value[i][0]
                        if value[j][0] == key:
                            new_val2 = value[j][1]
                        else:
                            new_val2 = value[j][0]
                        triple_tuple = (key, new_val1, new_val2)
                        if not present_in_triple(triple, triple_tuple):
                            triple.append(triple_tuple)
     

for line in triple:
    print(line)

print(len(triple))
                   

print(count_t(triple))