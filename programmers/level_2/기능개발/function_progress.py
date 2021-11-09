def solution(progresses, speeds):
    progresses2 = progresses.copy()  # 리스트 복사
    count_list = []
    result = []

    for i in range(len(progresses2)):
        count = 0  # 몇 번 더해야 100 넘는지
        while True:
            progresses2[i] = progresses2[i] + speeds[i]
            count += 1
            if progresses2[i] >= 100:
                break
        count_list.append(count)

    max = count_list[0]
    count2 = 1
    for j in range(1, len(count_list)):
        if max >= count_list[j]:
            count2 += 1
        else:
            result.append(count2)  # i번째가 i+1번째보다 작으면 result에 1 append -> count 1로 초기화 -> max값 i+1번째 값으로 바꿔줌
            count2 = 1
            max = count_list[j]
    result.append(count2)

    return result

# 시도해보다가 실패한 코드
#     for j in range(len(count_list)-2):
#         count2 = 1
#         if count_list[j] < count_list[j+1]:
#             result.append(1)
#         elif count_list[j] > count_list[j+1]:
#             for k in range(len(count_list)-2):
#                 if count_list[j] > count_list[j+1+k]:
#                     count2 +=1
#                 # print(count2)
#             # result.append(count2)
#         elif count_list[j] == count_list[j+1] :
#             result.append(2)