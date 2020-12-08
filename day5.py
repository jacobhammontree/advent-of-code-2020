import sys
import math
sys.path.append("./")

def calculate_seat_number(seat_string):
    rows = range(0,128)
    cols = range(0,8)
    for c in seat_string[:7]:
        if(c == "F"):
            rows = rows[:(len(rows)//2)]
        else:
            rows = rows[(len(rows)//2):]
    for c in seat_string[7:]:
        if(c == "L"):
            cols = cols[:(len(cols)//2)]
        else:
            cols = cols[(len(cols)//2):]
    return rows[0]*8+cols[0]

def calculate_all_seat_nums(seat_strings):
    ret = []
    for seat in seat_strings:
        if(seat.strip() == ""):
            continue
        ret.append(calculate_seat_number(seat.strip()))
    return ret

def get_max_seat_num(seat_nums):
    return max(seat_nums)

def find_missing_seat(sorted_seats):
    count = min(sorted_seats)
    for i in range(0, len(sorted_seats)):
        if count != sorted_seats[i]:
            return count
        count+=1
    return -1

f = open("./puzzle_inputs/day5.input")
seat_strings = f.readlines()

all_seat_nums = calculate_all_seat_nums(seat_strings)
print(get_max_seat_num(all_seat_nums))
sorted_seats = sorted(all_seat_nums)
print(find_missing_seat(sorted_seats))

