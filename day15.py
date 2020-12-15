import sys
from collections import defaultdict
sys.path.append("./")

def init_starting_nums(filename):
    f = open(filename)
    line = f.readline().strip()
    f.close()
    return [int(n) for n in line.split(",")]

def play_game(starting_nums, max_spoken_items):
    spoken = defaultdict(list)
    turn = 1
    # speak first round
    for n in starting_nums:
        spoken[n] = [turn]
        last_spoken = n
        turn+=1
    for i in range(len(starting_nums)+1, max_spoken_items+1):
        if last_spoken in spoken and len(spoken[last_spoken])>=2:
            last_spoken = spoken[last_spoken][-1] - spoken[last_spoken][-2]
        else:
            last_spoken = 0
        spoken[last_spoken].append(i)
    return last_spoken

s_nums = init_starting_nums("./puzzle_inputs/day15.input")
#part 1
print(play_game(s_nums, 2020))
#part 2
print(play_game(s_nums, 30000000))