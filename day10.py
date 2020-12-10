import sys
from collections import defaultdict
sys.path.append("./")

# returns a sorted list of adapters 
jump_map = {}
def init_adapter_list(filename):
    ret = []
    f = open(filename)
    line = f.readline().strip()
    while line:
        ret.append(int(line))
        line = f.readline().strip()
    ret.insert(0,0)
    return sorted(ret)

def count_steps(adapters):
    ret = defaultdict(int)
    curr = min(adapters[0:3])
    ret[curr]+=1
    done = False
    while not(done):
        if adapters.index(curr) == len(adapters)-1:
            done = True
            break
        next_step = min(adapters[adapters.index(curr)+1:adapters.index(curr)+4])
        ret[(next_step-curr)]+=1
        curr = next_step
    ret[3]+=1
    return ret

def count_paths(adapters):
    if len(adapters) == 0:
        return 0
    elif(len(adapters) == 1):
        return 1
    else:
        sum = 0
        poss_jumps = [n for n in adapters[1:] if n-adapters[0] <=3]
        for jump in poss_jumps:
            if jump in jump_map:
                sum+=jump_map[jump]
            else:
                jump_output = count_paths(adapters[adapters.index(jump):])
                jump_map[jump] = jump_output
                sum+= jump_output
        return sum

adapters = init_adapter_list("./puzzle_inputs/day10.input")
step_count = count_steps(adapters)
print(step_count[1] * step_count[3])
print(count_paths(adapters))