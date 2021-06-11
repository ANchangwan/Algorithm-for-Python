def solution(X, Y, D):
    position = Y - X
    jump_count = position // D
    if position % D == 0:
        return jump_count
    else:
        return jump_count +1 
