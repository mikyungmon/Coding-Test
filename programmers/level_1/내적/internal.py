def solution(a, b):
    sum_ = 0
    for i in range(len(a)):
        result = a[i] * b[i]
        sum_ += result
    return sum_

# 다른사람 풀이
# def solution(a, b):
#     return sum([x*y for x, y in zip(a,b)])