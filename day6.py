import sys
sys.path.append("./")

f = open("./puzzle_inputs/day6.input")

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

print(sum)