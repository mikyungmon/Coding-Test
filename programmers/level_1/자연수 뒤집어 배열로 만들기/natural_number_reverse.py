def solution(n):
    n_list = list(map(int, str(n)))
    answer = []
    for i in range(len(n_list)-1,-1,-1):  # len(n_list)-1에서 0까지 -1씩 숫자 감소
        answer.append(n_list[i])
    return answer

# 다른 사람 풀이 
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))  # reversed 생각 못함