import itertools
file = open('input_files/5.txt', 'r').read()
f = file.split("\n\n")

parsed_rules = [list(map(int, row.split("|"))) for row in f[0].split("\n")]
parsed_pages = f[1].split("\n")

def follows_rule(pages : list, rule : list) -> bool:
    first, second = rule[0], rule[1]
    firsts = [i for i in range(len(pages)) if pages[i] == first]
    seconds = [i for i in range(len(pages)) if pages[i] == second]
    return all ([(f < s) for f in firsts for s in seconds])

def correct_wrong(pages : list, rule : list) -> list :
    first, second = rule[0], rule[1]
    f, s = pages.index(first), pages.index(second)

    while(not(follows_rule(pages, rule))):
        if f > s:
            pages = reorder(pages, rule, f, s)
        
        # set new s
        if(pages[f+1:].count(second) > 0):
            s = pages.index(second, f+1)
        else:
            s = pages.index(second)
        
        # set new f
        if(pages[f+1:].count(first) > 0):
            f = pages.index(first, f+1)
        else:
            f = pages.index(first)
    return pages

def reorder(pages : list, rule : list, f : int, s : int) -> list:
    for i in range(s,f):
        pages[i]=pages[i+1]
    pages[f]=rule[1]
    return pages

count1 = 0
count2 = 0
for p in parsed_pages:
    original_conforms_to_rules = True
    pages = list(map(int, p.split(",")))
    original_midpoint = pages[int(len(pages)/2)]
    
    while (not all([follows_rule(pages, rule) for rule in parsed_rules])):
        for rule in parsed_rules:
            if pages.count(rule[0]) > 0 and pages.count(rule[1]) > 0:               
                if not follows_rule(pages, rule):
                    pages = correct_wrong(pages, rule)
                    original_conforms_to_rules = False

    if original_conforms_to_rules:
        count1 = count1 + original_midpoint
    else:
        count2 = count2 + pages[int(len(pages)/2)]
        
print("Part 1: ", str(count1))
print("Part 2: ", str(count2))

        
