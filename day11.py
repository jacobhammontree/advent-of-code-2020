import sys
from copy import deepcopy
sys.path.append("./")

def init_seat_map(file):
    f = open(file)
    line = f.readline().strip()
    ret = []
    while line:
        ret.append(list("F" + line + "F"))
        line = f.readline().strip()
    ret.insert(0,list("F"*len(ret[0])))
    ret.append(list("F"*len(ret[0])))
    return ret

def count_occupied_seats_part1(y, x, seatmap):
    ret = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if(i == 0 and j == 0):
                continue
            if(seatmap[y+i][x+j] == "#"):
                ret+=1
    return ret

def count_occupied_seats_part2(y,x,seatmap):
    ret = 0
    #n
    for y_ctr in range(y-1, -1, -1):
        if(seatmap[y_ctr][x] == "F" or seatmap[y_ctr][x] == "L"):
            break
        if(seatmap[y_ctr][x] == "#"):
            ret+=1
            break
            
    #ne
    x_ctr = x+1
    for y_ctr in range(y-1, -1, -1):
        if(seatmap[y_ctr][x_ctr] == "F" or seatmap[y_ctr][x_ctr] == "L"):
            break
        if(seatmap[y_ctr][x_ctr] == "#"):
            ret+=1
            break
        x_ctr+=1
    #e
    for x_ctr in range(x+1, len(seatmap[y])):
        if(seatmap[y][x_ctr] == "F" or seatmap[y][x_ctr] == "L"):
            break
        if(seatmap[y][x_ctr] == "#"):
            ret+=1
            break

    #se
    x_ctr = x+1
    for y_ctr in range(y+1, len(seatmap)):
        if(seatmap[y_ctr][x_ctr] == "F" or seatmap[y_ctr][x_ctr] == "L"):
            break
        if(seatmap[y_ctr][x_ctr] == "#"):
            ret+=1
            break
        x_ctr+=1
    #s
    for y_ctr in range(y+1, len(seatmap)):
        if(seatmap[y_ctr][x] == "F" or seatmap[y_ctr][x] == "L"):
            break
        if(seatmap[y_ctr][x] == "#"):
            ret+=1
            break
    #sw
    x_ctr = x-1
    for y_ctr in range(y+1, len(seatmap)):
        if(seatmap[y_ctr][x_ctr] == "F" or seatmap[y_ctr][x_ctr] == "L"):
            break
        if(seatmap[y_ctr][x_ctr] == "#"):
            ret+=1
            break
        x_ctr-=1
    #w
    for x_ctr in range(x-1, -1, -1):
        if(seatmap[y][x_ctr] == "F" or seatmap[y][x_ctr] == "L"):
            break
        if(seatmap[y][x_ctr] == "#"):
            ret+=1
            break
    #nw
    x_ctr = x-1 
    for y_ctr in range(y-1, -1, -1):
        if(seatmap[y_ctr][x_ctr] == "F" or seatmap[y_ctr][x_ctr] == "L"):
            break
        if(seatmap[y_ctr][x_ctr] == "#"):
            ret+=1
            break
        x_ctr-=1
    return ret

def simulate_seat_picking(seatmap, count_occ_seat = count_occupied_seats_part1, tolerance = 4):
    ret = deepcopy(seatmap)
    wc = deepcopy(seatmap)
    done = False
    while not done:
        done = True
        for y in range(1, len(ret)-1):
            for x in range(1, len(ret[y])-1):
                if wc[y][x] == ".":
                    continue
                occ_seats = count_occ_seat(y,x,ret)
                if occ_seats >= tolerance and wc[y][x] == "#":
                    wc[y][x] = "L"
                    done = False
                elif occ_seats == 0 and wc[y][x] == "L":
                    wc[y][x] = "#"
                    done = False
                else:
                    continue
        if not done:
            ret = wc
            wc = deepcopy(ret) 
    return ret

def count_full_seats(seatmap):
    ret = 0
    for i in range(0, len(seatmap)):
        for j in range(0, len(seatmap[i])):
            if seatmap[i][j] == "#":
                ret+=1
    return ret

filename = "./puzzle_inputs/day11.input"
seatmap = init_seat_map(filename)
done_seatmap = simulate_seat_picking(seatmap)
done_seatmap2 = simulate_seat_picking(seatmap,count_occupied_seats_part2, 5)
print(count_full_seats(done_seatmap))
print(count_full_seats(done_seatmap2))

