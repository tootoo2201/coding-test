arr = []
for i in range(10):
    num = int(input())
    mod = num % 42
    arr.append(mod)
result = len(set(arr))
print(result)