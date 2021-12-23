def solution(s):
    s_sort = sorted(s)  # str type은 sort메소드 없다. sorted(s)처럼 가능. 대신 return type은 list
    answer = []
    for i in range(len(s_sort)-1,-1,-1):
        answer.append(s_sort[i])

    return ("".join(answer))  # list -> str


# 다른사람 풀이

# def solution(s):
#     return ''.join(sorted(s, reverse=True))  # 내림차순 정렬 : sorted(reverse=True)