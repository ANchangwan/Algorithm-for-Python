def solution(X, Y, D):
    position = Y - X
    jump_count = position // D
    if position % D == 0:
        return jump_count
    else:
        return jump_count +1 
# 조건부 표현식
def solution(X, Y, D):
    position = Y - X
    jump_count = position // D
    
    return jump_count if position % D == 0 else jump_count + 1
