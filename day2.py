import sys
import re
sys.path.append("./")

def parse_password_and_policy(line):
    match = re.search(r"(\d+)-(\d+) (\w{1})\: (.*)", line)
    return [match.group(1), match.group(2), match.group(3), match.group(4)]

def is_valid_part1(policy):
    count_of_char = 0
    for c in policy[3]:
        if (c == policy[2]):
            count_of_char+=1
        if count_of_char>int(policy[1]):
            return False
    if(count_of_char>=int(policy[0])):
        return True
    return False

def is_valid_part2(policy):
    return (1 if (policy[3][int(policy[0])-1] == policy[2]) else 0) ^ (1 if (policy[3][int(policy[1])-1] == policy[2]) else 0)

def count_valid_passwords(passwordfile, valid_function = is_valid_part1):
    f = open(passwordfile)
    l = f.readline().replace("\n", "")
    count = 0
    while(l != ""):
        l_policy = parse_password_and_policy(l)
        if valid_function(l_policy):
            count+=1
        l = f.readline().replace("\n", "")    
    f.close()
    return count

print(count_valid_passwords("./puzzle_inputs/day2.input", is_valid_part1))
print(count_valid_passwords("./puzzle_inputs/day2.input", is_valid_part2))