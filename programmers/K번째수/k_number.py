def solution(array, commands):
    reg_array = []
    result = []

    for i in commands:
        # print(i)   # 출력 예시 : [2 5 3]
        reg_array.append(array[i[0] - 1:i[1]])

    for j in range(len(reg_array)):
        reg_array[j].sort()
        # print(reg_array) # 출력 예시:[[2, 3, 5, 6], [6], [1, 2, 3, 4, 5, 6, 7]]
        rank = commands[j][2]
        result.append(reg_array[j][rank - 1])
        print(result)

    return result