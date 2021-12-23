def solution(s):
    s = s.split(' ')  # s.split(): 공백을 기준으로 나뉜다 
    # s.split(' ') : ' ' 기준으로 나뉘지만 두 개인 경우는 첫번째 ' '로 나뉘고 두번째는 요소로 들어가게됨
    # "abc  dce" -> ['abc', ' ', 'dce'] 공백 두 개면 하나만 잘리고 하나는 리스트 안으로 들어가게됨
    
    result = []
    for i in range(len(s)):
        str_list = list(s[i])
        for j in range(len(s[i])):
            if j % 2 == 0:
                str_list[j] = str_list[j].upper()
            else:
                str_list[j] = str_list[j].lower()

        string = ''.join(str_list)
        result.append(string)  # 단어 하나하나 list마다 변환된 값 출력
    answer = ' '.join(result)
    return answer