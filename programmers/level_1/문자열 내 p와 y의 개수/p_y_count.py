def solution(s):
    p_counter = 0
    y_counter = 0
    for i in s:
        if i == 'p' or i == 'P':
            p_counter += 1
        elif i == 'y' or i == 'Y':
            y_counter += 1

    if p_counter == y_counter:
        return True
    else:
        return False

# 다른 사람 풀이
# 문자열을 소문자로 바꾼 뒤에 count함수 이용해서 p와 y 갯수 셈
# def numPY(s):
#     return s.lower().count('p') == s.lower().count('y')
