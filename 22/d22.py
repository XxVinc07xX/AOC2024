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


sum = 0
for line in lines:
    val = int(line)
    for _ in range(2000):
        res = secret_behavior(val)
        val = res
    #print(val)
    sum += val

print(sum)
