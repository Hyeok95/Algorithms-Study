def solution(board, moves):

    count = 0

    basket = []

    for i in moves:
        temp = 0
        j = 0
        while temp == 0 and j < len(board):
            if board[j][i - 1] != 0:
                temp = board[j][i - 1]
                board[j][i - 1] = 0
            else:
                j += 1

        if temp != 0:
            if len(basket) == 0:
                basket.append(temp)
            else:
                if temp == basket[-1]:
                    count += 2
                    del basket[-1]
                else:
                    basket.append(temp)

    return count