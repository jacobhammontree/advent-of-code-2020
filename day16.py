import sys
import re
from collections import defaultdict
sys.path.append("./")

# lst = list of lists2
# returns
#   flattened list containing all elements of all lists2
def flatten(lst):
    ret = []
    for l in lst:
        for e in l:
            ret.append(e)
    return ret
# args
#   ticket_filename (string) = name of the file that describes tickets and rules
# returns
#   rules (dictionary) PICK UP HERE
def init_rules_and_tickets(ticket_filename):
    f = open(ticket_filename)
    rules = {}
    line = f.readline().strip()
    while line:
        m = re.match(r"([a-zA-Z\s]+): (\d+)-(\d+) or (\d+)-(\d+)", line).groups(0)
        line = f.readline().strip()
        rules[m[0]] = [range(int(m[1]),int(m[2])+1), range(int(m[3]),int(m[4])+1)]
    
    ## read the "your ticket" line
    line = f.readline().strip()
    my_ticket_str = f.readline().strip()
    my_ticket = [int(n) for n in my_ticket_str.split(",")]

    ## read newline and "nearby tickets" lines
    line = f.readline()
    line = f.readline()

    ## below is the first line that has a nearby ticket
    line = f.readline().strip()
    nearby_tickets = []
    while line:
        nearby_tickets.append([int(n) for n in line.split(",")])
        line = f.readline().strip()

    f.close()
    return rules, my_ticket, nearby_tickets

# returns
#   0 if x is in one of the l_ranges
#   x if x is not in one of the l_ranges
def x_in_any(x, l_ranges):
    return 0 if any([x in l for l in l_ranges]) else x

# returns 
#   [0] the sum of ticket itmes that don't fall within any range
#   [1] a list of valid tickets
def calc_scanning_error_rate(rules, nearby_tickets):
    ret = 0
    valid_tickets=[]
    # get list of all ranges in a single list
    flat_ranges = flatten([v for v in rules.values()])
    for t in nearby_tickets:
        valid_ticket = True
        for e in t:
            to_add = x_in_any(e,flat_ranges)
            ret+=to_add
            if to_add:
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(t)
    return ret, valid_tickets

# returns true if 
#   all l in tnums are in within one of the two ranges
def all_ticket_values_match_range(t_nums, ranges):
    return all([n in ranges[0] or n in ranges[1] for n in t_nums])

# args
#   valid tickets = list of valid tickets (which are lists of numbers)
#   rules = dictionary<string->list<range>>
# returns
#   ticket_positions_poss = dict<string->list<int>>
#       key<string> = name of ticket item
#       value<list<int>> = list of possible ticket positions for key
def get_possible_ticket_positions(valid_tickets, rules):
    ticket_positions_poss = defaultdict(list)
    for r_name,r_ranges in rules.items():
        for i in range(0, len(my_ticket)):
            # if all ticket items for all tickets fall within the ranges of this rule, add index i as a possibility for this rule
            if(all_ticket_values_match_range([t[i] for t in valid_tickets], r_ranges)):
                ticket_positions_poss[r_name].append(i)
    return ticket_positions_poss

def get_ticket_positions(ticket_positions_poss):
    final_ticket_positions = {}
    # iterate while there are still possibilities
    while ticket_positions_poss:
        # returns a list of all items that have one possible index
        known_pos = [[t,v[0]] for t,v in ticket_positions_poss.items() if len(v) == 1]
        for kp in known_pos:
            # record the known index
            final_ticket_positions[kp[0]] = kp[1]
            # remove this ticket from the unknown (possible) list, since we know its position
            ticket_positions_poss.pop(kp[0])
            # for all other tickets, remove index i as a possibility
            for t_name,t_poss in ticket_positions_poss.items():
                if kp[1] in t_poss:
                    t_poss.remove(kp[1])
    return final_ticket_positions

def get_product_of_departure_fields(valid_tickets, rules, my_ticket):
    ticket_positions_poss = get_possible_ticket_positions(valid_tickets,rules)
    final_ticket_positions = get_ticket_positions(ticket_positions_poss)
    prd = 1
    for i in [poss for name,poss in final_ticket_positions.items() if re.match(r"^departure", name)]:
        prd*=my_ticket[i]
    return prd

rules,my_ticket,nearby_tickets = init_rules_and_tickets("./puzzle_inputs/day16.input")
err_rate,valid_tickets = calc_scanning_error_rate(rules,nearby_tickets)
valid_tickets.append(my_ticket)
#part 1
print(err_rate)
#part 2
part2 = get_product_of_departure_fields(valid_tickets, rules, my_ticket)
print(part2)