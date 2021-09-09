def solution(a, b):

    result = 0

    if b > a:
        for i in range(a,b+1):
            result +=i

    elif a == b:
        result = a

    else :
        for j in range(b,a+1):
            result +=j

    return result