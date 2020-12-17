import sys
import gc
import time
from collections import defaultdict
from copy import deepcopy

sys.path.append("./")

def print_z_level(pd, z):
    print("z = ",z)
    for i in range(min(pd[z].keys()), max(pd[z].keys())+1):
        y_keys = pd[z][i].keys()
        for j in range(min(y_keys), max(y_keys)+1):
            print(pd[z][i][j], end="")
        print("")
    return

def init_pocket_dimension(part2 = False,filename="./puzzle_inputs/day17.input"):
    if not part2:
        pocket_dimension = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda:".")))
        f = open(filename)
        y = 0
        line = f.readline().strip()
        while line:
            x = 0
            for c in line:
                pocket_dimension[0][y][x] = c
                x+=1
            y+=1
            line = f.readline().strip()
        f.close()
        return pocket_dimension
    else:
        pocket_dimension = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: "."))))
        f = open(filename)
        y = 0
        line = f.readline().strip()
        while line:
            x = 0
            for c in line:
                pocket_dimension[0][0][y][x] = c
                x+=1
            y+=1
            line = f.readline().strip()
        f.close()
        return pocket_dimension

def get_neighbors(z,y,x):
    ret = []
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                ret.append([z+i,y+j,x+k])
    return ret

def get_neighbors_part2(w,z,y,x):
    ret = []
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    ret.append([w+i,z+j,y+k,x+l])
    return ret

def count_active_neighbors(pd,z,y,x):
    neighbors = get_neighbors(z,y,x)
    count = 0
    for n_z,n_y,n_x in neighbors:
        if n_z == z and n_y == y and n_x == x:
            continue
        if(n_z in pd and n_y in pd[n_z] and n_x in pd[n_z][n_y] and pd[n_z][n_y][n_x] == "#"):
            count+=1
        else:
            pd[z][y][x]
    return count

def count_active_neighbors_part2(pd,w,z,y,x):
    neighbors = get_neighbors_part2(w,z,y,x)
    count = 0
    for n_w,n_z,n_y,n_x in neighbors:
        if n_w == w and n_z == z and n_y == y and n_x == x:
            continue
        if(n_w in pd and n_z in pd[n_w] and n_y in pd[n_w][n_z] and n_x in pd[n_w][n_z][n_y] and pd[n_w][n_z][n_y][n_x] == "#"):
            count+=1
        else:
            pd[w][z][y][x]
    return count

def init_neighbors(pd, neighbors):
    for n_z,n_y,n_x in neighbors:
        pd[n_z][n_y][n_x]

def init_neighbors_part2(pd, neighbors):
    for n_w,n_z,n_y,n_x in neighbors:
        pd[n_w][n_z][n_y][n_x]

def do_cycle(pd):
    pd_cp = deepcopy(pd)
    z_keys = pd_cp.keys()
    t0 = time.time()
    for z in range(min(z_keys), max(z_keys)+1):
        y_keys = pd_cp[z].keys()
        for y in range(min(y_keys), max(y_keys)+1):
            x_keys = pd_cp[z][y].keys()
            for x in range(min(x_keys), max(x_keys)+1):
                neighbors = get_neighbors(z,y,x)
                init_neighbors(pd,neighbors)
    t1 = time.time()
    print("init neighbors time ", t1-t0)
    del pd_cp
    pd_cp = deepcopy(pd)
    pd_cp2 = deepcopy(pd)
    z_keys= pd.keys()
    for z in range(min(z_keys), max(z_keys)+1):
        y_keys = pd[z].keys()
        for y in range(min(y_keys), max(y_keys)+1):
            x_keys = pd[z][y].keys()
            for x in range(min(x_keys), max(x_keys)+1):
                neighbor_count = count_active_neighbors(pd, z,y,x)
                if pd_cp2[z][y][x] == "#":
                    pd_cp[z][y][x] = "#" if neighbor_count in [2,3] else "."
                else:
                    pd_cp[z][y][x] = "#" if neighbor_count == 3 else "."
    del pd, pd_cp2
    return pd_cp

def do_cycle_part2(pd):
    pd_cp = deepcopy(pd)
    w_keys = pd_cp.keys()
    t0 = time.time()
    for w in range(min(w_keys), max(w_keys)+1):
        z_keys = pd_cp[w].keys()
        for z in range(min(z_keys), max(z_keys)+1):
            y_keys = pd_cp[w][z].keys()
            for y in range(min(y_keys), max(y_keys)+1):
                x_keys = pd_cp[w][z][y].keys()
                for x in range(min(x_keys), max(x_keys)+1):
                    neighbors = get_neighbors_part2(w,z,y,x)
                    init_neighbors_part2(pd,neighbors)
    t1 = time.time()
    print("init neighbors time ", t1-t0)
    del pd_cp
    pd_cp = deepcopy(pd)
    pd_cp2 = deepcopy(pd)

    w_keys = pd.keys()
    for w in range(min(w_keys), max(w_keys)+1):
        z_keys= pd[w].keys()
        for z in range(min(z_keys), max(z_keys)+1):
            y_keys = pd[w][z].keys()
            for y in range(min(y_keys), max(y_keys)+1):
                x_keys = pd[w][z][y].keys()
                for x in range(min(x_keys), max(x_keys)+1):
                    neighbor_count = count_active_neighbors_part2(pd, w,z,y,x)
                    if pd_cp2[w][z][y][x] == "#":
                        pd_cp[w][z][y][x] = "#" if neighbor_count in [2,3] else "."
                    else:
                        pd_cp[w][z][y][x] = "#" if neighbor_count == 3 else "."
    del pd, pd_cp2
    return pd_cp

def boot_up(pd,cycle=do_cycle):
    for _ in range(0,6):
        pd = cycle(pd)
    return pd

def count_all_active(pd):
    active_count = 0
    z_keys = pd.keys()
    for z in range(min(z_keys), max(z_keys)+1):
        y_keys = pd[z].keys()
        for y in range(min(y_keys), max(y_keys)+1):
            x_keys = pd[z][y].keys()
            for x in range(min(x_keys), max(x_keys)+1):
                if(pd[z][y][x] == "#"):
                    active_count+=1
    return active_count

def count_all_active_part2(pd):
    active_count = 0
    w_keys = pd.keys()
    n = 0
    for w in range(min(w_keys), max(w_keys)+1):
        z_keys = pd[w].keys()
        for z in range(min(z_keys), max(z_keys)+1):
            y_keys = pd[w][z].keys()
            for y in range(min(y_keys), max(y_keys)+1):
                x_keys = pd[w][z][y].keys()
                for x in range(min(x_keys), max(x_keys)+1):
                    if(pd[w][z][y][x] == "#"):
                        active_count+=1
                    n+=1
    return active_count,n

pd = init_pocket_dimension()
pd = boot_up(pd)
print(count_all_active(pd))

pd2 = init_pocket_dimension(True)
pd2 = boot_up(pd2, do_cycle_part2)
print(count_all_active_part2(pd2))
