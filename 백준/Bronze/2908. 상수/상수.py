first, second =input().split()
first_r = int(first[::-1]) #역순 [::-1]
second_r = int(second[::-1])
if (first_r > second_r):
    print(first_r)
else:
    print(second_r)