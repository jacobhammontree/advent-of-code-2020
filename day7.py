import sys
import re
from collections import defaultdict
import time
sys.path.append("./")

class Bag:
    def __init__(self, name="", parents=[], children=[]):
        self.name = name
        self.parents = parents
        self.children = children
    
    def __eq__(self, other):
        return self.name == other.name

    def count_all_ancestors(self):
        ret = []
        return ret
    
## returns dictionary of bags
def instantiate_bag_list(bag_file):
    bag_line = bag_file.readline().strip()
    bags = defaultdict(lambda:Bag(parents=[], children=[]))
    while bag_line:
        bag_array = [bag_line.split("contain")[0].strip().replace("bags","").strip()] + \
                    [s1.strip() for s1 in bag_line.split("contain")[1].strip().replace(".","").replace("bags","").replace("bag", "").split(",")]
        # initialize bag
        bags[bag_array[0]].name = bag_array[0]
        for b in bag_array[1:]:            
            if b == "no other":
                continue
            num, bag_name = re.match(r"(\d+) (.*)", b).groups(0)
            bags[bag_name].name = bag_name
            bags[bag_name].parents.append(bags[bag_array[0]])
            bags[bag_array[0]].children.append((bags[bag_name], int(num)))
        bag_line = bag_file.readline().strip()
    return dict(bags)

def count_all_ancestors(bag, bag_dictionary):
    subject = bag_dictionary[bag]
    visited = []
    to_consider = []
    to_consider += subject.parents
    while to_consider:
        curr = to_consider.pop(0)
        for gp in curr.parents:
            if gp not in visited:
                to_consider.append(gp)
        visited.append(curr)
    return len(set([v.name for v in visited]))

def count_nested_bags(bag, bag_dictionary):
    subject = bag_dictionary[bag]
    sum = 0
    for c in subject.children:
        sum = sum + c[1] + c[1] * count_nested_bags(c[0].name, bag_dictionary)
    return sum

f = open("./puzzle_inputs/day7.input")
bag_dictionary = instantiate_bag_list(f)

print(count_all_ancestors("shiny gold", bag_dictionary))

print(count_nested_bags("shiny gold", bag_dictionary))
