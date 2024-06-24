def solution(num_list):
    answer = num_list
    a = num_list[len(num_list)-1]
    b = num_list[len(num_list)-2]
    if(a > b):
        answer.append(a-b)
    else:
        answer.append(2*a)
    return answer