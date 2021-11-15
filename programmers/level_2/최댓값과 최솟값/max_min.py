def solution(s):
    list_str = s.split()  # 빈칸이 여러개여도 잘 나뉘는듯
    list_int = []
    result_max = 0
    result_min = 0

    for i in range(len(list_str)):
        list_int.append(int(list_str[i]))

    # min, max 굳이 이렇게 찾을 필요 없이 max(list_int), min(list_int)로도 가능
    max = list_int[0]
    min = list_int[0]

    for j in range(len(list_int)):
        if list_int[j] > max :
            max = list_int[j]
        elif list_int[j] < min :
            min = list_int[j]

    result_max = str(max)
    result_min = str(min)

    return (result_min + " " + result_max)

# 다른 사람 풀이
# def solution(s):
#     s = list(map(int,s.split()))     # map(function, iterable) -> map(적용시킬 함수, 적용할 값들). ex) map( 값에 +1 을 더해주는 함수, [1,2,3,4,5])
#     return str(min(s)) + " " + str(max(s))