from itertools import combinations


def solution(numbers):
    combi = list(combinations(numbers, 2))
    sum_value = []

    for i in range(len(combi)):
        sum_value.append(sum(combi[i]))

    print(sum_value)
    sum_value = list(sorted(set(sum_value)))  # sorted 없으면 안되는 경우 발생

    return sum_value