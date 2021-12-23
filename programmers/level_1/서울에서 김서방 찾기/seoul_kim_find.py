def solution(seoul):
    for i in range(len(seoul)):
        if 'Kim' == seoul[i]:
            i = str(i)   # int -> str
            a = '김서방은'
            b = i + '에'
            c = '있다'
            return ('{} {} {}'.format(a,b,c))

# 다른 사람 풀이
# def findKim(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))  # index(x)함수 : 리스트에 x값이 있으면 x의 위치값을 돌려준다
