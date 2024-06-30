def solution(cipher, code):
    answer = []
    for i in range(len(cipher)):
        if((i+1)%code==0):
            answer.append(cipher[i])
    answer = ''.join(answer)
    return answer