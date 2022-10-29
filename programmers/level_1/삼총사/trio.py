from itertools import combinations


def solution(number):
    combi = list(combinations(number, 3))
    trio = 0

    for i in range(len(combi)):
        if sum(combi[i]) == 0:
            trio += 1

    return trio