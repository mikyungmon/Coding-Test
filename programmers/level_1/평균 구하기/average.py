def solution(arr):
    sum = 0
    avg = 0
    for i in range(len(arr)):
        sum += arr[i]

    avg = sum / len(arr)

    return avg

# 다른 사람 풀이
# def average(list):
#     return (sum(list) / len(list))