def solution(num):
    if(num == 1):
        return 0
    cnt = 0
    n = 0
    while(n < 500):
        if(num%2==0):
            num /= 2
            cnt += 1
        elif(num%2==1):
            num = num * 3 + 1
            cnt += 1
        n += 1
        if(num == 1):
            return cnt
            break
    return -1
            