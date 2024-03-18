T = int(input())
for i in range(T):
    n, st = input().split()
    stlist = list(st)
    for i in stlist:
        print(i*int(n), end='')
    print()