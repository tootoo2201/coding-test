arr=[]
while True:
    N = int(input())
    if (N == -1):
        break
    for i in range(1, N):
        if(N % i == 0):
            arr.append(i)
    if(sum(arr) == N):
        print(N," = "," + ".join(str(i) for i in arr), sep="")
    else:
        print(N,"is NOT perfect.")
    arr = []