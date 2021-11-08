while 1:
    try:
        a , b = int(input()), list(map(int,input().split()))
        if b != " ":
            c = sorted(b)
            d = []
            for i in range(a):
                if c[i] != b[i]:
                    d.append(b[i])
            start = b.index(d[0])
            end  = b.index(d[-1])
            if (b[:start] + list(reversed(b[start:end+1])) + b[end+1:] == c):
                print('yes')
            else:
                print('no')
    except:
        break