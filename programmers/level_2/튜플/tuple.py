# 답 참고
def solution(s):
    result = []
    s = s[2:-2]  # 앞,뒤로 '{{' 와 '}}' 삭제
    s = s.split('},{')
    s.sort(key = len)   # 길이 작은거부터 sort -> 오름차순 정렬

    for i in s:
        ii = i.split(',')  # list 형태로 반환(ii -> ex.['3'] / ['2', '3'] ~~)
        for j in ii:
            if int(j) not in result:  # int(j) 예시 : 2 , 3
                result.append(int(j))

    return result

# 내 풀이(시간초과로 60점인 코드)
# def solution(s):
#     result = []
#     new_s = s[1:len(s)-1]
#     new_s = new_s.split('},{')
#
#     a = str(new_s[0])
#     if '{' in a or '}' in a :
#         a = a.replace('}',"")
#         a = a.replace('{',"")
#     new_s[0] = a
#
#     b = str(new_s[-1])
#     if '{' in b or '}' in b :
#         b = b.replace('}',"")
#         b = b.replace('{',"")
#     new_s[-1] = b
#
#     ddaom = []
#     for x in range(len(new_s)):
#         ddaom.append(new_s[x].count(','))
#
#     for i in range(len(new_s)):
#         if new_s[i].count(',') == 0:
#             result.append(int(new_s[i]))
#
#     for y in range(1, max(ddaom)+1):
#         for j in range(len(new_s)):
#             if new_s[j].count(',') == y:
#                 c = (new_s[j].split(','))
#                 for k in range(len(c)):
#                     c[k] = int(c[k])
#
#                 for p in range(len(result)):
#                     for u in range(len(c)):
#                         if c[u] not in result :
#                             result.append(c[u])
#
#     return result