def solution(board, moves):
    answer = 0
    result = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0

                if len(result) > 1:
                    if result[-1] == result[-2]:
                        result.pop(-1)
                        result.pop(-1)
                        answer += 2
                break  # board[j][i-1] == 0: 일 때 중지!!

    return answer
