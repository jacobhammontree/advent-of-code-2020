import sys
import re
from math import ceil,floor
from copy import deepcopy
sys.path.append("./")

def init_bus_file(filename, part1 = True):
    f = open(filename)
    arrival_mins = int(re.match(r"(\d+)",f.readline().strip()).groups(0)[0])
    if part1:
        buses = [int(re.match(r"(\d+)",s.strip()).groups(0)[0]) for s in f.readline().split(",") if re.match(r"(\d+)", s)]
    else:
        num_x = 0
        buses = []
        s = f.readline().strip()
        for e in s.split(","):
            m = re.match(r"(\d+)",e)
            if m:
                buses.append((int(m.groups(0)[0]),num_x))
                num_x+=1
            else:
                num_x+=1
    f.close()
    return arrival_mins,buses

def find_next_bus(busfile):
    a = [busfile[0]%a for a in busfile[1]]
    idx = a.index(max(a))
    val = busfile[1][idx]
    wait_time = floor((ceil(busfile[0]/val)-busfile[0]/val)*val)
    return val,wait_time

def product(lst):
    prd = 1
    for e in lst:
        prd*=e
    return prd

def find_cont_timestamp(buses):
    bus_list = deepcopy(buses[1])
    i = 0
    prd = buses[1][0][0]
    working_list = [bus_list.pop(0)]
    while bus_list:
        working_list.append(bus_list.pop(0))
        found = False
        while not found:
            cont = False
            for b,x in working_list:
                if((i+x) % b != 0):
                    cont = True
                    break
            if cont:
                i+=prd
                continue
            else:
                found = True
        if bus_list:
            prd = product([b for b,_ in working_list])
        else:
            return i
    return 0

busfile = init_bus_file("./puzzle_inputs/day13.input")
next_bus = find_next_bus(busfile)
print(next_bus[0]*next_bus[1])
busfile2 = init_bus_file("./puzzle_inputs/day13.input", False)
print(busfile2)
timestamp = find_cont_timestamp(busfile2)
print(timestamp)

