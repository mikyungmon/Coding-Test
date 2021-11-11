# 답 참고
import itertools


def solution(numbers):
    def is_prime(num):  # 소수 판별 함수
        if num < 2:  # 0,1은 소수 아니므로 false
            return False
        else:
            # 에라토스테네스의 체 이용
            # 2부터 num의 제곱근까지 모든 수를 확인하며 num이 i로 나눠지면 i 제외하고 다 제거
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

    temp = set()  # set : 집합 자료형(중복허용x, 순서x)

    for i in range(1, len(numbers) + 1):
        for j in itertools.permutations(numbers, i):  # number를 1개로 구성된 순열, 2개로 구성된 순열,,~ 해서 numbers갯수로 구성된 순열 만들기
            comb_num = int("".join(j))
            if is_prime(comb_num):
                temp.add(comb_num)
        print(temp)

    return len(temp)

# 실패 코드 : 2,10번 시간초과, 4번 틀림 -> 75점
# import itertools
# from itertools import permutations
#
#
# def solution(numbers):
#     each_num = []
#     data2 = []
#     data3 = []
#     comb_num = []
#     new_comb_num = []
#     new_comb_num2 = []
#     count = []
#
#     for i in range(len(numbers)):
#         each_num.append(numbers[i])
#
#     for j in range(1, len(each_num) + 1):
#         data = list(permutations(each_num, j))
#         data2.append(data)
#
#     for k in range(len(data2)):
#         data3 = list(itertools.chain(*data2))  # 2차원->1차원 list로
#
#     for z in range(len(data3)):
#         if len(data3[z]) > 1:
#             comb_num.append("".join(data3[z]))
#         else:
#             comb_num.append("".join(data3[z][0]))
#
#     for a in comb_num:  # 중복제거
#         if a not in new_comb_num:
#             new_comb_num.append(a)
#
#     for b in range(len(new_comb_num)):
#         if len(new_comb_num[b]) > 1:
#             if int(new_comb_num[b][0]) == 0:
#                 new_comb_num[b] = "".join(new_comb_num[1:len(new_comb_num[b])])
#
#     for c in new_comb_num:  # 중복제거
#         if c not in new_comb_num2:
#             new_comb_num2.append(c)
#
#     for f in range(len(new_comb_num2)):
#         count.append(0)
#
#     for d in range(len(new_comb_num2)):
#         for e in range(2, int(new_comb_num2[d]) + 1):
#             if int(new_comb_num2[d]) % e == 0:
#                 count[d] += 1
#
#     result = 0
#     for g in range(len(count)):
#         if count[g] == 1:
#             result += 1
#
#     return result
