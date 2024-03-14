N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]
change = 0
for i in range(M):
    f, s = map(int,input().split())
    change = arr[f-1]
    arr[f-1] = arr[s-1]
    arr[s-1] = change
for i in range(N):
    print(arr[i], end=" ")
