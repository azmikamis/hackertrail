def findnextseat(n,taken):
    longestgapstart = 0
    longestgaplength = 0
    gapstart = 0
    gaplength = 0
    for i,j in enumerate(sorted(taken)):
        if len(taken) == 0:
            longestgapstart = 1
            longestgaplength = n
        
        if i == 0:
            gapstart = 1 if j != 1 else j+1
            if i == len(taken)-1:
                gaplength = n-gapstart if j != n else n-gapstart-1
        else:    
            if i == len(taken)-1:
                gaplength = n-gapstart-1 if j != n else n-gapstart
            else:
                gaplength = j-gapstart

        if gaplength > longestgaplength:
            longestgaplength = gaplength
            longestgapstart = gapstart
        gapstart = j+1

    if longestgapstart == 1:
        return 1
    elif longestgapstart + longestgaplength == n and n not in taken:
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

