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

def BronKerbosch(R,P,X): #https://fr.wikipedia.org/wiki/Algorithme_de_Bron-Kerbosch
    if len(P) == 0 and len(X) == 0:
        complete_graphs.append(R)
    for sommet in list(P):
        BronKerbosch(R | {sommet}, P & dic[sommet], X & dic[sommet])
        P.remove(sommet)
        X.add(sommet)




dic={}

for line in lines:
    #print(line)
    line = line.split("-")
    line[1] = line[1].strip()
    tuple_line = (line[0], line[1])
    #print(tuple_line)
    if line[0] not in dic:
        dic[line[0]] = set()

    if line[1] not in dic:
        dic[line[1]] = set()
    
    if line[1] not in dic[line[0]]:
        dic[line[0]].add(line[1])
    
    if  line[0] not in dic[line[1]]:
        dic[line[1]].add(line[0])

#print(dic)

complete_graphs = []

BronKerbosch(set(), set(dic.keys()),set())


maxConnection = max(complete_graphs, key=len)
print(sorted(maxConnection))
