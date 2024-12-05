import itertools
file = open('input_files/5.txt', 'r').read()
lines = file.splitlines()

f = file.split("\n\n")
parsedRules = [ row.split("|") for row in f[0].split("\n")]
parsedPages = f[1].split("\n")

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

def followsRule(pages : list, rule : list) -> bool:
    first = rule[0]
    second = rule[1]
    firsts = [i for i in range(len(pages)) if pages[i] == first]
    seconds = [i for i in range(len(pages)) if pages[i] == second]
    for f in firsts:
        for s in seconds:
            if f > s:
                return False
    return True

def correctWrong(pages : list, rule : list) -> list :
    first = rule[0]
    second = rule[1]
    pages2 = pages
    f = pages.index(first)
    s = pages.index(second)

    while(not(followsRule(pages, rule))):
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
    second = rule[1]
    for i in range(s,f):
        pages[i]=pages[i+1]
    pages[f]=second
    return pages

count1 = 0
count2 = 0
for p in parsedPages:
    followsrule = True
    pages = p.split(",")
    firstmiddle = int(findMiddle(pages))
    followsallrules = False
    
    while (not followsallrules):
        for rule in parsedRules:
            if pages.count(rule[0]) > 0:
                if not followsRule(pages, rule):
                    pages = correctWrong(pages, rule)
                    followsrule = False
                    followsallrules = False
        followsallrules = all([followsRule(pages, rule) for rule in parsedRules])

    if followsrule:
        count1 = count1 + firstmiddle
    else:
        count2 = count2 + int(findMiddle(pages))
        
print("Part 1: " + str(count1))
print("Part 2: " + str(count2))

        
