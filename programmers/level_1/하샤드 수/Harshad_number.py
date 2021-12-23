def solution(x):
    x_list = list(map(int, str(x)))
    sum = 0
    for i in range(len(x_list)):
        sum += x_list[i]

    if x % sum == 0:
        return True
    else:
        return False

# 다른 사람 풀이
# def Harshad(n):
#     # n은 하샤드 수 인가요?
#     return n % sum([int(c) for c in str(n)]) == 0
