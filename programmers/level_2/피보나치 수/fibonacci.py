# 재귀호출 사용하면 시간초과 및 오류발생
def solution(n):
    result = [0, 1]
    for i in range(2, n + 1):  # point! 굳이 i범위 2~100000까지 할 필요없고 n까지만 하면 됨
        result.append((result[i - 1] + result[i - 2]) % 1234567)  # point! 배열 안에 추가될 떄는 %1234567 계산까지 한 후에 추가

    return result[-1]  # 마지막 결과를 return