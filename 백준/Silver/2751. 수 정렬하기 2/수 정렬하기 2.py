import sys
N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)
arr1 = sorted(arr)
for i in range(N):
    print(arr1[i])