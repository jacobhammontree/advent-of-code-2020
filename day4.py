import sys
import re
sys.path.append("./")

# file must be opened prior to passing it in
def get_single_passport(file):
    passport_lines = []
    line = file.readline().replace("\n", "")
    while(line != ""):
        passport_lines.append(line)
        line = file.readline().replace("\n", "")
    ret = ""
    for l in passport_lines:
        ret = ret + " " + l
    return ret.strip()

def validate_passport(passport, part2_check = False):
    required_set = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    passport_string = passport.split(" ")
    passport_tokens = []
    for pt in passport_string:
        passport_tokens.append(pt.split(":"))
    for k,v in passport_tokens:
        try:
            required_set.remove(k)
        except:
            pass
        if(part2_check):
            try:
                if(k == "byr"):
                    if not(int(v) >= 1920 and int(v) <= 2002): 
                        return False
                if(k == "iyr"):
                    if not(int(v)>=2010 and int(v)<=2020):
                        return False
                if(k == "eyr"):
                    if not(int(v)>=2020 and int(v)<=2030):
                        return False
                if(k == "hgt"):
                    units = re.match(r"^(\d+)(cm|in)$", v)
                    if not(units):
                        return False
                    else:
                        if(units.groups(0)[1] == "in"):
                            if(not(int(units.groups(0)[0])>= 59 and int(units.groups(0)[0]) <=76)):
                                return False
                        else:
                            if(not(int(units.groups(0)[0])>= 150 and int(units.groups(0)[0]) <=193)):
                                return False
                if(k == "hcl"):
                    m = re.match(r"^#[0-9a-f]{6}$", v)
                    if(not(m)):
                        return False
                if(k == "ecl"):
                    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if (v not in eye_colors):
                        return False
                if(k == "pid"):
                    m = re.match(r"^\d{9}$", v)
                    if(not(m)):
                        return False
            except:
                return False
    if(required_set == set()):
        return True       
    return False


def count_valid_passports(filename, part2_check = False):
    f = open("./puzzle_inputs/day4.input")
    count = 0
    passport = get_single_passport(f)
    while passport != "":
        count = count + 1 if validate_passport(passport, part2_check) else count
        passport = get_single_passport(f)
    f.close()
    return count

num_valid_passports = count_valid_passports("./puzzle_inputs/day4.input", True)
