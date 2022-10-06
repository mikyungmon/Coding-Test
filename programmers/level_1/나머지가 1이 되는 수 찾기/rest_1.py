def solution(n):
    n2 = n-1
    list_ = []
    for i in range(1,n):
        if n2 % i == 0 :
            list_.append(i)

    return list_[1]

# 다른사람 풀이
# def solution(n):
#     return [x for x in range(1,n+1) if n%x==1][0]