input_file = open("d19_input.txt")
lines = input_file.readlines()

patterns = lines[0].strip()
patterns_list = list(patterns.split(", "))
patterns_dic = dict((pat, 0) for pat in patterns_list)

count = 0
designs = lines[2:]

def can_form_string(target, patterns_dic, memo):
    if target in memo:  # Return cached result
        return memo[target]
    if target == '': 
        return True
    
    for pattern, max_count in patterns_dic.items():
        if max_count > 0 and target.startswith(pattern):
            # Use the pattern, reducing its count
            patterns_dic[pattern] -= 1
            if can_form_string(target[len(pattern):], patterns_dic, memo):
                memo[target] = True
                return True
            patterns_dic[pattern] += 1  # Backtrack if it didn't work
    
    memo[target] = False  #keep track that it did not work
    return False


for i in range(len(designs)):
    line = designs[i].strip()
    
    for key in patterns_dic.keys():
        patterns_dic[key] = line.count(key)
    
    # Use memoization https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/
    memo = {}
    if can_form_string(line, patterns_dic, memo):
        count += 1

print(count)



