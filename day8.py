import sys
import re
from copy import deepcopy
sys.path.append("./")

def init_input_array(input_file):
    ret = []
    line = input_file.readline().strip()
    while line:
        command, num = re.match(r"([a-z]{3}) (.*)", line).groups(0)
        ret.append([command, int(num)])
        line = input_file.readline().strip()
    return ret


def execute_program(instruction_array):
    curr_instruction = 0
    acc = 0
    visited = []
    loop_found = False
    while not(loop_found) and curr_instruction < len(instruction_array):
        if (curr_instruction in visited):
            loop_found = True
            break
        if (instruction_array[curr_instruction][0] == "nop"):
            visited.append(curr_instruction)
            curr_instruction+=1
        elif (instruction_array[curr_instruction][0] == "acc"):
            acc+=instruction_array[curr_instruction][1]
            visited.append(curr_instruction)
            curr_instruction+=1
        elif (instruction_array[curr_instruction][0] == "jmp"):
            visited.append(curr_instruction)
            if instruction_array[curr_instruction][1] == 0:
                loop_found = True
                break
            curr_instruction+=instruction_array[curr_instruction][1]
    return [acc,loop_found]

def fix_program(instruction_array):
    curr = 0
    acc = -1
    fixed = False
    while not(fixed) or curr < len(instruction_array):
        ia_copy = deepcopy(instruction_array)
        while (ia_copy[curr][0] != "jmp" and ia_copy[curr][0] != "nop"):
            curr+=1
        if(ia_copy[curr][0] == "jmp"):
            ia_copy[curr][0] = "nop"
        else:
            ia_copy[curr][0] = "jmp"
        acc, loop_found = execute_program(ia_copy.copy())
        if(not loop_found):
            break
        curr+=1
    return acc

f = open("./puzzle_inputs/day8.input")
instruction_array = init_input_array(f)
f.close()
print(execute_program(instruction_array.copy()))

print(fix_program(instruction_array))