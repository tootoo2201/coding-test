def solution(money):
    ame = money//5500
    change = money%5500
    answer = [ame, change]
    return answer