N = int(input())
arr=[]
result=[]
for i in range(N):
    a = input()
    arr.append(a)
for i in arr:
    if i not in result:
        result.append(i)
result.sort()
result.sort(key=len)
for i in result : print(i)