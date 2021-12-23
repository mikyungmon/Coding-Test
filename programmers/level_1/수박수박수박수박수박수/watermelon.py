def solution(n):
    a = '수'
    b = '박'
    c = []
    result = []
    for i in range(5000):
        c.append(a)
        c.append(b)

    for j in range(n):
        result.append(c[j])

    result = ("".join(result))

    return result

# 다른 사람 풀이
# def water_melon(n):
#     s = "수박" * n
#     return s[:n]