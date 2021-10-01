def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        result = []
        for answer in s:
            if answer.isdigit():
                result.append('true')
            else:
                result.append('false')
        if 'false' in result:
            return False
        else:
            return True
    else:
        return False