def solution(answers):
    answer1 = []
    answer2 = []
    answer3 = []

    result1 = 0  # 사람 당 맞춘 문제 수
    result2 = 0
    result3 = 0

    rank = []

    x = 0
    y = 0
    z = 0

    while (x < 10000):
        answer1.append(1)
        answer1.append(2)
        answer1.append(3)
        answer1.append(4)
        answer1.append(5)
        x += 1

        # print(answer1)

    while (y < 1250):
        answer2.append(2)
        answer2.append(1)
        answer2.append(2)
        answer2.append(3)
        answer2.append(2)
        answer2.append(4)
        answer2.append(2)
        answer2.append(5)
        y += 1

    while (z < 1000):
        answer3.append(3)
        answer3.append(3)
        answer3.append(1)
        answer3.append(1)
        answer3.append(2)
        answer3.append(2)
        answer3.append(4)
        answer3.append(4)
        answer3.append(5)
        answer3.append(5)
        z += 1

        # 답지 개수만큼 자름
    answer1 = answer1[0:len(answers)]
    answer2 = answer2[0:len(answers)]
    answer3 = answer3[0:len(answers)]

    for x in range(len(answers)):
        if answer1[x] == answers[x]:
            result1 += 1

        if answer2[x] == answers[x]:
            result2 += 1

        if answer3[x] == answers[x]:
            result3 += 1

    if (result1 > result2) and (result1 > result3):
        rank.append(1)

    elif (result2 > result1) and (result2 > result3):
        rank.append(2)

    elif (result3 > result1) and (result3 > result2):
        rank.append(3)

    elif (result1 == result2) and (result1 > result3):
        rank.append(1)
        rank.append(2)

    elif (result1 == result3) and (result1 > result2):
        rank.append(1)
        rank.append(3)

    elif (result2 == result3) and (result2 > result1):
        rank.append(2)
        rank.append(3)

    elif (result1 == result2 == result3):
        rank.append(1)
        rank.append(2)
        rank.append(3)

    return rank