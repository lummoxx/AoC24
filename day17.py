
file = open('input_files/17.txt', 'r').read()
[regs, ins] = file.split("\n\n")

def group(ls : list, n : int) -> list :
    return [ls[i:i+3] for i in range(0, len(ls), 3)]

program = list(map(int, ins.split(":")[1].replace(" ", "").split(",")))
registers = regs.split("\n")
reg_a = int(registers[0].split(":")[1].replace(" ", ""))
reg_b = int(registers[1].split(":")[1].replace(" ", ""))
reg_c = int(registers[2].split(":")[1].replace(" ", ""))

instruction_pointer = 0

def combo(lit : int): # = { 0:1, 1:1, 2:2, 3:3, 4 : reg_a, 5: reg_b, 6: reg_c, 7:None}
    global reg_a, reg_b, reg_c
    if lit in  [0,1,2,3]:
        return lit
    elif lit == 4:
        return reg_a
    elif lit == 5:
        return reg_b
    elif lit == 6:
        return reg_c

# 0
def a_divide_by_2_pow_combo(operand : int):
    global reg_a
    numerator = reg_a
    denominator = pow(2, combo(operand))
    reg_a = int(numerator/denominator)
# 1
def bitwise_xor_b_literal(operand : int):
    global reg_b 
    reg_b ^= operand
# 2   
def calc_combo_modulo_8_to_b(operand : int):
    global reg_b
    reg_b = combo(operand) % 8

# 3   
def nothing_if_a_not_zero(operand : int):
    global reg_a, instruction_pointer
    if reg_a != 0:
        instruction_pointer = operand
# 4   
def bitwise_xor_b_c(operand : int):
    global reg_b, reg_c
    reg_b ^= reg_c

# 5   
def return_combo_modulo_8(operand : int):
    out = combo( operand ) % 8
    return out

# 6   
def quotient_to_b(operand : int):
    global reg_b, reg_a
    reg_b = int(reg_a/pow(2, combo( operand )))

# 7   
def quotient_to_c(operand : int):
    global reg_c, reg_a
    reg_c  = int(reg_a/pow(2, combo( operand )))

instructions = {0: a_divide_by_2_pow_combo, 1: bitwise_xor_b_literal, 
                2: calc_combo_modulo_8_to_b, 3: nothing_if_a_not_zero, 
                4: bitwise_xor_b_c, 5: return_combo_modulo_8, 
                6 : quotient_to_b, 7: quotient_to_c}

def run_program():
    global instruction_pointer
    while instruction_pointer < len(program):
        current = instruction_pointer
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        output = instructions[opcode](operand)
        if output is not None:
            yield output
        if instruction_pointer == current:
            instruction_pointer += 2
    return

output = run_program()
print(list(output))
",".join(map(str, output))
