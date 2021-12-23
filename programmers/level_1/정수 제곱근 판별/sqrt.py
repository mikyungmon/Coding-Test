import math


def solution(n):
    answer = 0
    sq = math.sqrt(n)  # 제곱근
    if sq % 1 == 0:  # 제곱근이 양의 정수이면 해당조건 만족할 것
        answer = (sq + 1) * (sq + 1)
        return answer
    else:
        return -1

# 다른 사람 풀이
# def nextSqure(n):
#     sqrt = n ** (1/2) # ** (1/2) : 제곱근
#
#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2  # ** 2 : 제곱
#     return 'no'