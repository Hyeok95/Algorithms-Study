def solution(board, moves):
    answer = 0
    result = []
    for index in moves:
        a = len(board[index-1])
        for i in range(a):
            if board[i][index-1] != 0:
                result.append(board[i][index-1])
                board[i][index-1] =0
                break
        if len(result) >= 2 and result[-2] == result[-1]:
            result.pop()
            result.pop()
            answer += 2
                
    return answer