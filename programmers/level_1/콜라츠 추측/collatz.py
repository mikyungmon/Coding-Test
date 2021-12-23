def solution(num):
    count = 0
    for i in range(50000):
        if num == 1:
            break
        elif num % 2 == 0:
            num = num // 2
            count += 1
            if num == 1:
                break
            elif num % 2 == 1 and num != 1:
                num = num * 3 + 1
                count += 1
                if num == 1:
                    break
        else:
            num = num * 3 + 1
            count += 1
            if num % 2 == 0:
                num = num // 2
                count += 1
            elif num == 1:
                break

    if count <= 500:
        return count
    else:
        return -1

# 다른 사람 풀이
# def collatz(num):
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num*3 + 1
#         if num == 1:
#             return i + 1
#     return -1