import re
import numpy as np
from decimal import Decimal

games = open('input_files/13.txt', 'r').read().split("\n\n")

def get_x_y(line : str) -> tuple[int, int]:
    entities = line.split(":")[1].split()
    return (int(re.findall(r'\d+', entities[0])[0]), int(re.findall(r'\d+', entities[1])[0]))

def is_almost_integer(value, tol=1e-3): 
    return abs(value - round(value)) < tol

def check_leading_zeros(value, zeroes_count=4): 
    str_value = str(value)
    if '.' not in str_value: 
        return True
    fractional_part = str_value.split('.')[-1]
    return fractional_part.startswith('0' * zeroes_count)

def integer_solutions(a :  tuple[int, int], b :  tuple[int, int], p :  tuple[int, int]) -> int:
    tokens = 0
    (ax, ay) = a
    (bx, by) = b
    (px, py) = p
    A = np.array(([[ax, bx], [ay, by]]))
    
    # part 1:
    y1 = np.array([px, py])
    # part 2:
    y2 = np.array([px+10000000000000, py+10000000000000])
    x = np.linalg.lstsq(A, y1, rcond=None)[0]
    
    x_0 = check_leading_zeros(Decimal(x[0])) or is_almost_integer(Decimal(x[0]))
    x_1 = check_leading_zeros(Decimal(x[1])) or is_almost_integer(Decimal(x[1])) 

    if x_0 and x_1 :
        integer_values = np.rint(x).astype(int)
        tokens = (integer_values[0]*3)+integer_values[1]
    return int(tokens+0.5)
    
print(integer_solutions((0,0), (0,0), (0,0)))
tokens = 0
for i,g in enumerate(games):
    [a, b, p] = [ get_x_y(n) for n in g.split("\n")]
    tokens += integer_solutions(a, b, p)
print(tokens)