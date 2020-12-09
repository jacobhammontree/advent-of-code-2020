import sys
sys.path.append("./")

def sum_found(lst, num):
    s = set()
    for n in lst:
        if(abs((num-n)) in s):
            return True
        s.add(n)
    return False

def find_improper_number(input_array, n=25):
    prev_n = [x for x in input_array[:n]]
    queue = input_array[n:]
    to_check = queue.pop(0) if len(queue) > 0 else None
    while to_check is not None:
        if(sum_found(prev_n, to_check)):
            prev_n.pop(0)
            prev_n.append(to_check)
            to_check = queue.pop(0) if len(queue) > 0 else None
        else:
            return to_check
    return -1

def format_list(filename):
    f = open(filename)
    line = f.readline().strip()
    ret = []
    while line:
        ret.append(int(line))
        line = f.readline().strip()
    return ret

def find_contiguous_set(n, lst):
    ret = []
    found = False
    while not found:
        if(sum(ret) < n):
            ret.append(lst.pop(0))
        elif(sum(ret) > n):
            ret.pop(0)
        else:
            break
    return ret

lst = format_list("./puzzle_inputs/day9.input")
num = find_improper_number(lst, 25)
print(num)
cont_set = find_contiguous_set(num, lst)
print(min(cont_set)+max(cont_set))