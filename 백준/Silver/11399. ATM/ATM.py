N = int(input())
arr = list(map(int,input().split()))
arr.sort()
answer = 0
for i in range(1,N+1):
    answer += sum(arr[:i])
print(answer)