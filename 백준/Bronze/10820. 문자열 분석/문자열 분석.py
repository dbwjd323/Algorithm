import sys

while True:
    N = sys.stdin.readline().rstrip('\n')
    
    if not N:
        break
    
    low, upper, num, space = 0, 0, 0, 0

    for i in N:
        if i.islower():
            low += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        else:
            space += 1
    print(low, upper, num, space)
        