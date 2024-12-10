import math
file = open('input_files/7.txt', 'r').read()
lines = file.splitlines()

def cal(n : int, nums : list, test_value : int):
    if len(nums) > 0 and n <= test_value:
        m = nums[0] 
        for operation in [n * m, n + m, math.pow(10,(int(math.log(m,10)) + 1)) * n + m]:
            yield from cal(operation, nums[1:], test_value)
    else:
        yield n

result = 0
for l in lines:
    nums = list(map(int, l.replace(":", "").strip().split(" ")))
    if nums[0] in cal(nums[1], nums[2:], nums[0]):
        result += nums[0]
print(result)
