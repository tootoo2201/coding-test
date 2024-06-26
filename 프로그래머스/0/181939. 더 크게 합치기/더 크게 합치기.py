def solution(a, b):
    f = int(str(a)+str(b))
    s = int(str(b)+str(a))
    if (f>s):
        return f
    else:
        return s