def solution(phone_number):
    for i in range(len(phone_number) - 4):
        phone_number = phone_number.replace(phone_number[i], '*',1)  # 세 번째 인자 : 입력을 하지 않으면 찾은 모든 문자를 변경하고, 특정 횟수만 변경하고 싶다면 숫자를 집어넣으면 된다
    return phone_number

# 다른 사람 풀이
# def hide_numbers(s):
#     return "*"*(len(s)-4) + s[-4:]