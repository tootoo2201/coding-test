def solution(dot):
    a = dot
    if a[0] > 0 and a[1] > 0:
        return 1
    elif a[0] < 0 and a[1] > 0:
        return 2
    elif a[0] < 0 and a[1] < 0:
        return 3
    else:  
        return 4
  