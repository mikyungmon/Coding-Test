def solution(s):

    answer = s
    ch_figure = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    matching = []

    for i in range(10):  # 숫자를 뜻하는 문자열과 숫자 matching
        matching.append((ch_figure[i],i))
    # print(matching[0][0])  # zero 출력됨

        # print(matching[i][0])

        if str(matching[i][0]) in answer :
            answer = answer.replace(str(matching[i][0]),str(matching[i][1]))
    # print(answer)
    return int(answer)