def solution(arr, divisor):

    result = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            result.append(arr[i])
            result.sort()

    if len(result) == 0:
        result.append(-1)

    return result