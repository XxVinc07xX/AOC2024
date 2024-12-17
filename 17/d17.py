input = open("d17_input.txt","r")
lines = input.readlines()

def combo_operand(reg_A, reg_B, reg_C, operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return reg_A
    elif operand == 5:
        return reg_B
    elif operand == 6:
        return reg_C
    return None


def behavior(instr_ptr, opcode, operand, reg_A, reg_B, reg_C, prog_limit, out):
    if opcode == 0:
        operand = combo_operand(reg_A=reg_A, reg_B=reg_B, reg_C=reg_C, operand=operand)
        reg_A = int(reg_A/(2**operand))
        instr_ptr += 2
        return (instr_ptr, reg_A, reg_B, reg_C, out)
    elif opcode == 1:
        reg_B = reg_B ^ operand
        instr_ptr += 2
        return (instr_ptr, reg_A, reg_B, reg_C, out)
    elif opcode == 2:
        operand = combo_operand(reg_A=reg_A, reg_B=reg_B, reg_C=reg_C, operand=operand)
        inter = operand%8
        reg_B =  int(inter & 0b111) 
        instr_ptr += 2
        return (instr_ptr, reg_A, reg_B, reg_C, out)
    elif opcode == 3:
        if reg_A != 0:
            if operand <= prog_limit:
                instr_ptr = operand
                return (instr_ptr, reg_A, reg_B, reg_C, out)
        else:
            return None
    elif opcode == 4:
        reg_B = reg_B ^ reg_C
        instr_ptr += 2
        return (instr_ptr, reg_A, reg_B, reg_C, out)
    elif opcode == 5:
        operand = combo_operand(reg_A=reg_A, reg_B=reg_B, reg_C=reg_C, operand=operand)
        instr_ptr += 2
        out += str(operand%8) + ','
        return (instr_ptr, reg_A, reg_B, reg_C, out)
    elif opcode == 6:
        operand = combo_operand(reg_A=reg_A, reg_B=reg_B, reg_C=reg_C, operand=operand)
        reg_B = int(reg_A/(2**operand))
        instr_ptr += 2
        return (instr_ptr, reg_A, reg_B, reg_C, out)
    elif opcode == 7:
        operand = combo_operand(reg_A=reg_A, reg_B=reg_B, reg_C=reg_C, operand=operand)
        reg_C = int(reg_A/(2**operand))
        instr_ptr += 2
        return (instr_ptr, reg_A, reg_B, reg_C, out)



        


out=""

reg_A = int(lines[0].split(":")[1])
reg_B = int(lines[1].split(":")[1])
reg_C = int(lines[2].split(":")[1])

prog = lines[4].split(": ")[1]
prog = list(prog.replace(',',''))
prog_limit = len(prog)-2 #-2 to place instr_ptr on the opcode

instr_ptr = 0

while (instr_ptr != None):
    res = behavior(instr_ptr,opcode=int(prog[instr_ptr]),operand=int(prog[instr_ptr+1]),reg_A=reg_A,reg_B=reg_B, reg_C=reg_C,prog_limit=prog_limit, out=out)
    if res != None:
        instr_ptr = res[0]
        reg_A = res[1]
        reg_B = res[2]
        reg_C = res[3]
        out = res[4]
    else:
        break

out = out[:-1]

print("out", out)

