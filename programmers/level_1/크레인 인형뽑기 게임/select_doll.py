def solution(board, moves):
    count = 0  # 사라지는 인형 개수
    box = []
    # print(len(board))  # 열 수 

    for i in moves:  # 열 번호 선택
        for j in range(len(board)):  # 행 이동
            if board[j][i - 1] != 0:
                box.append(board[j][i - 1])
                board[j][i - 1] = 0
                # print(box)
                break

        if len(box) > 1:
            if box[len(box) - 1] == box[len(box) - 2]:
                box.pop()
                box.pop()
                count += 2

    return count