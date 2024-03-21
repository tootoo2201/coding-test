while True:
    f, s = map(int, input().split())
    if (f == 0 and s == 0):
        break;
    if (f%s == 0):
        print("multiple")
    elif(s%f == 0):
        print("factor")
    else:
        print("neither")