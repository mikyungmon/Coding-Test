def solution(sizes):
    garo = []
    sero = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:   # 해당 조건을 생각해내지 못함(답 참고)
            garo.append(sizes[i][0])
            sero.append(sizes[i][1])
        else:
            sero.append(sizes[i][0])
            garo.append(sizes[i][1])

    return max(garo) * max(sero)

