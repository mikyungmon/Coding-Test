# 재귀호출 사용하면 시간초과 및 오류발생
def solution(n):
    result = [0, 1]
    for i in range(2, n + 1):  # point! 굳이 i범위 2~100000까지 할 필요없고 n까지만 하면 됨
        # 자료형의 크기에 제한이 있는 언어를 쓸 경우 (A + B) % C ≡ ( ( A % C ) + ( B % C) ) % C라는 성질을 이용해서 매번 계산 결과에 1234567으로 나눈 나머지를 대신 넣는 것으로 int 범위 내에 항상 값이 존재함을 보장할 수 있음
        result.append((result[i - 1] + result[i - 2]) % 1234567)  # point! 배열 안에 추가될 떄는 %1234567 계산까지 한 후에 추가

    return result[-1]  # 마지막 결과를 return