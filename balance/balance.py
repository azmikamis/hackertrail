t = int(raw_input())
tests = [raw_input() for _ in range(t)]

for s in tests:
    i = 0
    p = []
    n = []
    nstr = ''
    balanced = True
    while i < len(s):
        sym = s[i]
        if sym == '[':
            p.append(sym)
        elif sym == ',':
            if nstr != '':
                n.append(nstr)
                nstr = ''
        elif sym == ']':
            if nstr != '':
                n.append(nstr)
                nstr = ''
            p.pop()
            r = n.pop()
            l = n.pop()
            if len([x for x in (l, r) if "?" in x]) == 2:
                if len(p) > 0:
                    j = l.count("?")
                    k = r.count("?")
                    n.append("?" * max(j, k) * 2)
            elif len([x for x in (l, r) if "?" in x]) == 1:
                a = [x for x in (l, r) if "?" not in x][0]
                b = [x for x in (l, r) if "?" in x][0]
                if int(a) % b.count("?") != 0:
                    balanced = False
                    break
                else:
                    if len(p) > 0:
                        n.append(str(int(a) * 2))
            else:
                if int(r) != int(l):
                    balanced = False
                    break 
                else:
                    if len(p) > 0:
                        n.append(str(int(r) + int(l)))
        else:
            nstr += sym 
        i += 1
    print "YES" if balanced else "NO"
