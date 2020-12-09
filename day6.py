import sys
from collections import defaultdict
sys.path.append("./")

def count_any(f):
    line = f.readline().strip()
    sum = 0
    s = set()
    while line != "":
        if(line == "\n"):
            sum += len(s)
            s = set()
            line = f.readline()
            continue
        for c in line.strip():
            s.add(c)
        line = f.readline()
    sum+=len(s)  
    return sum

def count_all(f):
    line = f.readline()
    num_in_group = 0
    answers = defaultdict(lambda:0)
    all_sum = 0
    while line != "":
        if(line == "\n"):
            # do something see if everyone said yes
            group_sum = 0
            for v in answers.values():
                if v == num_in_group:
                    group_sum+=1
            all_sum+=group_sum
            group_sum=0
            answers = defaultdict(lambda:0)
            num_in_group = 0
            line = f.readline()
            continue
        for c in line.strip():
            answers[c] += 1
        num_in_group+=1
        line = f.readline()

    group_sum = 0
    for v in answers.values():
        if v == num_in_group:
            group_sum+=1
    all_sum+=group_sum
    return all_sum

f = open("./puzzle_inputs/day6.input")
print(count_any(f))
f.close()
f = open("./puzzle_inputs/day6.input")
print(count_all(f))
f.close()