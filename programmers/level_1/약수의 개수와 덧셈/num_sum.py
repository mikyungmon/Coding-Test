def solution(left, right):
    num = []
    counts = []  # 약수 개수 리스트
    sum_num = 0
    
    # left ~ right 사이 수 num 리스트에 저장
    for i in range(left, right + 1):
        num.append(i)

    for j in num:
        count = 0
        for k in range(1, j + 1):
            if j % k == 0:
                count += 1
        counts.append(count)

    for a in range(len(counts)):
        if counts[a] % 2 == 0:
            sum_num += num[a]
        else:
            sum_num -= num[a]

    return sum_num

# 다른 사람 풀이
# 제곱수를 제외한 모든 정수들의 약수 개수는 무조건 짝수 개수이며 제곱수만 홀수 개수 -> 이걸 이용
# ex) 2를 제곱근으로 갖는 4는 1,2,4해서 약수가 3개(홀수), 10의 제곱근은 3.1622776601683795 으로 정수가 아님.
#     10의 약수는 1,2,5,10 이렇게 4개(짝수)
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer