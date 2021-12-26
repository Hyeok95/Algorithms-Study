def solution(board, moves):
    answer = []
    stack = []
    
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                
                if stack[-1:] == stack[-2:-1]:
                    answer += stack[-1:]
                    stack = stack[:-2]
                break
    return len(answer)*2
