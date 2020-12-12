import sys
import re
sys.path.append("./")

dirs = ["N", "E", "S", "W"]

def init_instructions(filename):
    ret = []
    f = open(filename)
    line = f.readline().strip()
    while line:
        m = re.match(r"([A-Z])(\d+)", line)
        ret.append((m.groups(0)[0], int(m.groups(0)[1])))
        line = f.readline().strip()
    f.close()
    return ret

def travel(dir, n, coords):
    if dir == "N":
        coords[0]+=n
    if dir == "S":
        coords[0]-=n
    if dir == "E":
        coords[1]+=n
    if dir == "W":
        coords[1]-=n
    return coords

def execute_travel(instructions, dir_facing = "E", coords = [0,0]):
    coordinates = coords
    dir = dir_facing
    for d,n in instructions:
        direction = d if (d in dirs or d in ["L","R"]) else dir
        travel(direction,n,coordinates)
        if direction == "R":
            dir = dirs[abs((dirs.index(dir)+(n//90)))%4]
        if direction == "L":
            dir = dirs[(dirs.index(dir)-(n//90))%4]

    return coordinates

def execute_travel_part2(instructions):
    waypoint = [1, 10]
    ship_coords = [0,0]
    for d,n in instructions:
        if d in dirs:
            waypoint = travel(d, n, waypoint)
        if d == "R":
            for _ in range(0, n//90):
                waypoint = [-waypoint[1], waypoint[0]]
        if d == "L":
            for _ in range(0, n//90):
                waypoint = [waypoint[1], -waypoint[0]]
        if d == "F":
            ship_coords = [ship_coords[0]+n*waypoint[0],ship_coords[1]+n*waypoint[1]]
    print(waypoint)
    return ship_coords

instructions = init_instructions("./puzzle_inputs/day12.input")
print(instructions)
new_coords = execute_travel(instructions)
print(abs(new_coords[0]) + abs(new_coords[1]))
new_coords_part2 = execute_travel_part2(instructions)
print(abs(new_coords_part2[0]) + abs(new_coords_part2[1]))