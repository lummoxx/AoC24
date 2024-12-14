
from collections import defaultdict
from collections import namedtuple

file = open('input_files/14.txt', 'r').read()
lines = file.splitlines()

# w, h = (11, 7)
w, h = (101, 103)
mw, mh = (w-1)/2, (h-1)/2

Pos = namedtuple("Pos", ["x", "y"])
Robot = namedtuple("Robot", ["pos", "v"])

def move_until_tree(robots : list)-> int:
    seconds = 0
    while(True):
        new_robots = []
        positions = defaultdict(int)
        for r in robots:
            new_pos = move_one(r)
            positions[new_pos] += 1
            new_robots.append(Robot(new_pos, r.v))
        seconds += 1
        if len([p for p in positions.values() if p > 1]) == 0:
            break
        robots = new_robots
    return seconds
    
def move_one(r : Robot)-> Robot:
    (x, y) = r.pos
    (vx, vy) = r.v
    (new_x, new_y) = (x+vx, y+vy)
    new_pos = (new_x % w, new_y % h)
    return new_pos

def move(r : Robot, sec : int) -> tuple[int, int]:
    (x, y) = r.pos
    (vx, vy) = r.v
    (new_x, new_y) = (x+vx*sec, y+vy*sec)
    new_pos = (new_x % w, new_y % h)
    return new_pos
    
def get_x_y(line : str) -> tuple[int, int]:
    nums = line.split("=")[1].split(",")
    return (int(nums[0]),int(nums[1]))

positions = defaultdict(int)
robots = []

for l in lines:
    p = get_x_y(l.split()[0])
    v = get_x_y(l.split()[1])
    r = Robot(p, v)
    robots.append(r)
    positions[move(r, 100)] += 1

count = 0
quadrants = defaultdict(int)
for p in positions:
    (x,y) = p
    if x < mw and y < mh:
        quadrants[1] += positions[p]
    if x < mw and y > mh:
        quadrants[3] += positions[p]
    if x > mw and y < mh:
        quadrants[2] += positions[p]
    if x > mw and y > mh:
        quadrants[4] += positions[p]

print(quadrants[1]*quadrants[2]*quadrants[3]*quadrants[4])
print(move_until_tree(robots))
