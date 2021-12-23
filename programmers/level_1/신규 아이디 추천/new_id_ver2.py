# 정규식 이용하는 version

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)  # 문자 클래스 안에 ^는 not 의미
    st = re.sub('\.+', '..', st)

    # ^python 인 경우 문자열의 처음은 항상 python 으로 시작해야 매치되고,
    # 만약 정규식이 python$이라면 문자열의 마지막은 항상 python 으로 끝나야 매치된다는 의미
    st = re.sub('^[.]|[.]$', '', st) # ^는 문자열 처음 의미, $는 문자열 마지막 의미

    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)  # ^는 문자열 처음 의미, $는 문자열 마지막 의미
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])

    return st

