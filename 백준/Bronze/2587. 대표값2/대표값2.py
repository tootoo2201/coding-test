arr1 =[]
for i in range(5):
    N = int(input())
    arr1.append(N)
print(sum(arr1)//5)
arr2 = sorted(arr1)
print(arr2[2])