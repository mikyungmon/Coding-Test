def solution(n, m):
    min_value = []  # 최소공배수
    max_value = []  # 최대공약수
    same = []
    same2 = []

    # 최대공약수
    for i in range(1, max(n, m) + 1):
        if n % i == 0 and m % i == 0:
            same.append(i)
    max_value.append(max(same))

    # 최소공배수
    for j in range(max(n, m), n * m + 1): # ex. n : 12, m :10 -> 12 ~ 120까지 1씩 커지면서 둘 다 나머지가 0인 수 중 가장 작은 수 찾기
        if j % n == 0 and j % m == 0:
            same2.append(j)
    min_value.append(min(same2))

    return max_value + min_value
