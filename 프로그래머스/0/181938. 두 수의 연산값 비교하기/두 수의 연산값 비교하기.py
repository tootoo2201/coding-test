def solution(a, b):
    f = int(str(a)+str(b))
    s = 2*a*b
    if(f>s):
        return f
    else:
        return s