def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]

    return sum(absolutes)

# 다른사람 풀이
# zip 함수 - 여러 개의 iterable 객체를 받은 후 자료형 들을 묶어서 튜플 형태로 출력
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))