def findnextseat(n,taken):
    longestgapstart = 0
    longestgaplength = 0
    gapstart = 0
    gaplength = 0

    if len(taken) == 0:
        return 1
    
    l = sorted(taken)
    if l[0] != 1:
        l.insert(0, 0)
    if l[len(l)-1] != n:
        l.append(n+1)

    for i,j in enumerate(l):
        if i == 0:
            gapstart = j+1
            continue
        else:    
            gaplength = j-gapstart

        if gaplength > longestgaplength:
            longestgaplength = gaplength
            longestgapstart = gapstart
        gapstart = j+1

    if longestgapstart == 1:
        return 1
    elif longestgapstart + longestgaplength - 1 == n and n not in l:
        return n
    else:
        return longestgapstart + (longestgaplength-1)/2

t = int(raw_input())
for _ in range(t):
    m, n = map(int, raw_input().split())
    x = int(raw_input())
    k = int(raw_input())
    s = map(int, raw_input().split())

    taken = [x]
    result = []
    if 1 in s:
        result.append(str(x))
        k -= 1

    for i in range(2,n+1):
        if k == 0:
            break
        nextseat = findnextseat(m,taken)
        if i in s:
            result.append(str(nextseat))
            k -= 1
        taken.append(nextseat)

    print ' '.join(result)

