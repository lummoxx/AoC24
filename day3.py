
import math
import re

file = open('input_files/3.txt', 'r')
lines = file.read()

def muls(ls : str) -> int:
    result = 0
    pattern = r"mul\([0-9]+,[0-9]+\)"
    muls = re.findall(pattern, ls)
    for m in muls:
        # factors = map(int, m.replace("mul(", "").replace(")", "").split(","))
        factors = map(int, re.sub(r"mul\(|\)", "", m).split(","))
        result = result + math.prod(factors)
    return result
final = 0


donts = lines.split("don't()")
final = final + muls(donts[0])
for d in donts[1:]:
    dos = d.find("do()")
    final = final + muls(d[dos:])
print(final)
        
    