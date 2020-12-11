import sys
sys.path.append("./")

def hit_tree(level, x):
    return level[x] == "#"

def count_tree_collisions(map, xslope = 3, yslope = 1):
    count = 0
    x = 0
    f = open(map)
    level = f.readline().replace("\n", "")
    while level != "":
        count = (count+1) if(hit_tree(level, x % len(level))) else count
        x += xslope
        try:
            for _ in range(0, yslope):
                level = f.readline().replace("\n", "")
        except:
            break
    f.close()
    return count

input_filename = "./puzzle_inputs/day3.input"
print(count_tree_collisions(input_filename))

print(count_tree_collisions(input_filename, 1, 1) * \
      count_tree_collisions(input_filename, 3, 1) * \
      count_tree_collisions(input_filename, 5, 1) * \
      count_tree_collisions(input_filename, 7, 1) * \
      count_tree_collisions(input_filename, 1, 2))