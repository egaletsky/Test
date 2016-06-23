n = int(input())
ls = []
a = 0

while len(ls) < n:
    a += 1

    for i in range(a):
        ls.append(a)

        i += 1

print(' '.join(str(v) for v in ls[:n]))