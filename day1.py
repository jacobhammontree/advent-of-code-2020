import sys
sys.path.append("./")

def sum_of_2(filename, target=2020): # part 1
    f = open(filename)
    n = f.readline().replace("\n", "")
    s = set()
    while(n != ""):
        if(target-int(n) in s):
            f.close()
            return [int(n),(target-int(n))]
        else:
            s.add(int(n))
        n = f.readline().replace("\n", "")
    f.close()
    return [-1,-1]

def sum_of_3(filename, target): # part 2
    f = open(filename)
    n = f.readline().replace("\n", "")
    while(n != ""):
        of_two = sum_of_2(filename, target-int(n))
        if(of_two[0]>0):
            return [int(n)] + of_two
        n = f.readline().replace("\n", "")
    return -1

