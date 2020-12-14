import sys
import re
from itertools import permutations
sys.path.append("./")

def apply_mask(n,mask, part2 = False):
    if not part2:
        return (int(n)&int(mask.replace("X","1"),2)) | int(mask.replace("X","0"),2)
    else:
        nm = n|int(mask.replace("X", "1"),2)
        nm_s = "{0:b}".format(nm).zfill(36) 
        nm_sb = ""
        for i in range(0,36):
            if mask[i] == "X":
                nm_sb += "X"
            else:
                nm_sb+=nm_s[i]
        return nm_sb

def split_on_x(addr):
    ret = []
    i = 0
    sb = ""
    for i in range(0, len(addr)):
        sb+=addr[i]
        if(addr[i] == "X"):
            ret.append(sb)
            sb = ""
    ret.append(sb)
    return ret

def init_memory(instruction_file):
    mem = {}
    f = open(instruction_file)
    line = f.readline().strip()
    mask = ""
    while line:
        if line[:4] == "mask":
            mask = re.match(r"mask = (.*)",line).groups(0)[0]
        else:
            m_addr,n = re.match(r"mem\[(\d+)\] = (.*)",line).groups(0)
            mem[m_addr] = apply_mask(n,mask)
        line = f.readline().strip()
    f.close()
    return mem

def replace_x(mask):
    ret = []
    for i in ["1","0"]:
        ret.append(mask.replace("X", i))
    return ret

def perm_lists(p_groups):
    idx = len(p_groups)-2
    combs = p_groups[idx:idx+2]
    while idx>=0:
        p_groups[idx] = perm_2_lists(combs)
        idx-=1
        combs = p_groups[idx:idx+2]
    return p_groups[0]

def enumerate_mem_addrs(mask):
    p_groups = []
    mask_split = split_on_x(mask)
    for ms in mask_split:
        group = []
        for rx in replace_x(ms):
            group.append(rx)
        p_groups.append(group)
    return p_groups

def perm_2_lists(lst):
    ret = []
    for i in lst[0]:
        for j in lst[1]:
            ret.append(i + j)
    return ret

def init_memory_part_2(instruction_file):
    mem2 = {}
    f = open(instruction_file)
    line = f.readline().strip()
    mask = ""
    while line:
        if line[:4] == "mask":
            mask = re.match(r"mask = (.*)",line).groups(0)[0]
        else:
            m_addr,n = re.match(r"mem\[(\d+)\] = (.*)",line).groups(0)
            masked_addr = apply_mask(int(m_addr),mask,True)
            ps = enumerate_mem_addrs(masked_addr)
            address_list = perm_lists(ps)
            for e in address_list:
                mem2[int(e)] = int(n)
        line = f.readline().strip()
    f.close()
    return mem2

# part 1
memory = init_memory("./puzzle_inputs/day14.input")
print(sum(memory.values()))

# part 2
memory2 = init_memory_part_2("./puzzle_inputs/day14.input")
print("new sum:",sum(memory2.values()))
