def solution(numbers):
    no = []    # 없는 수 
    for i in range(10):
        if i not in numbers :
            no.append(i)

    return(sum(no))

# 다른사람 풀이
# 1부터 9까지 합인 45에서 나머지 숫자의 합들을 뺴줌
# def solution(numbers):
#     return 45 - sum(numbers)