# 답 참고
from collections import deque


def solution(priorities, location):
    prior = 0  # 순서
    prior_queue = deque((value, index) for index, value in enumerate(priorities))

    while prior_queue:
        item = prior_queue.popleft()

        if prior_queue and max(prior_queue)[0] > item[0]:  # 맨 왼쪽 튜플의 value 값보다 남은 애들 중 value값이 더 큰 튜플이 있다면 맨 왼쪽 튜플을 맨 오른쪽으로 보낸다
            prior_queue.append(item)
        else:
            prior += 1   # 맨 왼쪽 value 값이 더 크거나 같으면 순서를 1부터 카운팅한다
            if item[1] == location:   # 순서 카운팅 하다가 location(내가 요청한 서류 순서의 인덱스번호)이 일치하는 튜플의 순서를 반환
                break

    return prior

# 하다가 잘 안된 코드 (정답률 50)
# def solution(priorities, location):
#     priorities_idx = list(enumerate(priorities))
#     priorities_idx.sort(key=lambda x: x[1], reverse=True)
#
#     result = []
#     min_value = []
#
#     for j in range(len(priorities_idx)):
#         result.append(0)
#
#     max_idx = priorities_idx[0][0]
#     result[priorities_idx[0][0]] = 1
#     index_value = 1
#
#     for i in range(1, len(priorities_idx)):
#         if max_idx < priorities_idx[i][0]:
#             index_value += 1
#             result[priorities_idx[i][0]] = index_value
#
#         elif max_idx > priorities_idx[i][0]:
#             min_value.append(priorities_idx[i])
#
#     print(min_value)
#     for k in range(len(min_value) - 1):
#         if min_value[k][1] >= min_value[k + 1][1]:
#             index_value += 1
#             result[min_value[k][0]] = index_value
#             index_value += 1
#             result[min_value[k + 1][0]] = index_value
#         else:
#             index_value += 1
#             result[min_value[k + 1][0]] = index_value
#             index_value += 1
#             result[min_value[k][0]] = index_value
#
#     return result[location]
