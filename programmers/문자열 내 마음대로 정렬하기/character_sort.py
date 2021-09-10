# 답 참고

def solution(strings, n):
    ch = []
    strings2 = []
    cut = []

    # 각 문자열의 인덱스 n번째 글자를 strings 맨 앞에 붙이고 정렬
    for i in range(len(strings)):
        ch.append(strings[i][n])
        strings2.append(ch[i] + strings[i])
        strings2.sort()
        print(strings2)

    # 정렬 후 앞에 붙인 글자 제외하고 return
    for j in range(len(strings2)):
        cut.append(strings2[j][1:])

    return cut