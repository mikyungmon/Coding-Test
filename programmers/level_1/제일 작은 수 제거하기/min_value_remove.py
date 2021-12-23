def solution(arr):
    min = arr[0]
    answer = []
    answer2 = []
    for i in range(len(arr)):
        if min >= arr[i]:
            min = arr[i]

    arr.remove(min)

    if arr == [] :
        answer2.append(-1)
        return answer2

    return arr

# 다른 사람 풀이 (return -1 고려되지 않은 문제)
# def rm_small(mylist):
#     mylist.remove(min(mylist))
#     return mylist