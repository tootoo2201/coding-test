def solution(num_list):
    a=num_list[0]
    s=sum(num_list)
    for i in range(1,len(num_list)):
        a = a*num_list[i]
    if (a < s**2):
        return 1
    else:
        return 0
    