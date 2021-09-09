def solution(s):

    result = []

    if len(s) % 2 == 0:
        half = len(s) / 2
        half = int(half)
        result.append(s[half - 1])
        result.append(s[half])
        result = "".join(result)  # list -> str

    else:
        half = len(s) / 2
        half = int(half)
        result.append(s[half])
        result = "".join(result)

    return result