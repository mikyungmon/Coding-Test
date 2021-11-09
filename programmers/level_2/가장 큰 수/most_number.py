# 정답 참고
def solution(numbers):
    result = ''
    numbers2 = [str(i) * 3 for i in numbers]  # 원소 길이 곱하기 3, 왜 3을 곱하는지 이해 못함
    numbers3 = list(enumerate(numbers2))   # 각 원소에 인덱스 번호 묶어 튜플 생성
    numbers3.sort(key=lambda x:x[1], reverse=True)  # x:x[1] -> (0,1) 이면 1 기준으로 정렬, 문자열 비교는 아스키코드 기준
    for index, value in numbers3:
        result += str(numbers[index])   # 인덱스 이용하여 result 만들기

    return str(int(result))     # [0,0,0,0,0,0]의 형태일 때, 결과는 "0"이 나와야하므로 int -> str 과정 해줘야 함