file = open('input_files/7.txt', 'r').read()
lines = file.splitlines()

def cal(n : int, nums : list, result : int):
    if len(nums) > 0 and n <= result:
        p = n * nums[0] 
        s = n + nums[0] 
        c = int(str(n) + str(nums[0])) 
        yield from cal(p, nums[1:], result)
        yield from cal(s, nums[1:], result)
        yield from cal(c, nums[1:], result)
    else:
        yield n

final = 0
for l in lines:
    res, terms = l.split(":")
    nums = [ int(s) for s in terms.strip().split(" ")]
    result = int(res)
    if any([ n == result for n in cal(nums[0], nums[1:], result)]):
        final += result
print(final)