def check(basket):
    if 1 < len(basket):
        if basket[len(basket) - 2] == basket[len(basket) - 1]:
            basket.pop()
            basket.pop()
            return True


def solution(board, moves):
    answer = 0
    crain = 0
    basket = []
    for move in moves:
        while crain < len(board):
            if board[crain][move - 1] == 0:
                crain += 1
            else:
                basket.append(board[crain][move - 1])
                board[crain][move - 1] = 0
                crain = 0
                if check(basket):
                    answer += 2
                break
        if crain == 5:
            crain = 0

    return answer