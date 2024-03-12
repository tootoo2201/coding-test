N,M = map(int, input().split())
list_N = [0]*(N+1)
for i in range(M):
    first, final, ball = map(int, input().split())
    for n in range(first, final+1):
        list_N[n] = ball
for i in range(1, N+1):
    print(list_N[i], end =' ')