def solution(new_id):
    answer = ""

    # 1. 소문자 만들기
    new_id = new_id.lower()

    # 2. 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제외
    for ch in new_id:
        if ch.islower() or ch.isdigit() or ch in ["-", "_", "."]:
            answer += ch  # 위 조건에 충족한 것들만 answer에 넣음

    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 변경
    while '..' in answer:
        answer = answer.replace('..', '.')
        print(answer)

    # 4. 마침표가 id의 끝이나 처음에 위치하면 제거

    if answer[0] == ".":
        if len(answer) >= 2:
            answer = answer[1:]  # 1은 인덱스 넘버

    if answer[-1] == ".":
        answer = answer[:-1]  # 마지막 인덱스 이전까지 포함

    # 5. id가 빈 문자열이면 id에 "a" 대입

    if answer == "":
        answer = "a"

    # 6. id길이가 16자 이상이면 첫 15개의 문자를 제외하고 나머지 제외. 제외 후 마침표가 id의 끝에 위치하면 마침표 제거

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7. id길이가 2자 이하라면 id의 마지막 문자를 id길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(answer) <= 2:
        answer += answer[-1]

    return answer