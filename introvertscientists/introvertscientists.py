def findnextseat(n,taken):
    longestgapstart = 0
    longestgaplength = 0
    gapstart = 0
    gaplength = 0
    for i in range(1,n+1):
        if len(taken) == 0:
            longestgapstart = 1
            longestgaplength = n

        if i in taken:
            if gaplength > longestgaplength:
                longestgaplength = gaplength
                longestgapstart = gapstart 
            gaplength = 0
        else:
            if i == n:
                if gaplength > longestgaplength:
                    longestgaplength = gaplength
                    longestgapstart = gapstart 
            else:
                if gaplength == 0:
                    gapstart = i
                gaplength += 1

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
    for i in range(n-1):
        taken.append(findnextseat(m,taken))

    result = []
    for i in s:
        result.append(str(taken[i-1]))

    print ' '.join(result)
