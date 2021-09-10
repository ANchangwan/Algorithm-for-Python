def solution(N, stages):
    answer = []
    chellenge = len(stages)
    
    for x in range(1, N+1):
        c = stages.count(x)
        if c == 0:
            fail = 0
            
        else:
            fail = c / chellenge
            chellenge -= c
        answer.append((x, fail))
    answer.sort(key=lambda x:x[1], reverse=True)
    answer = [x[0] for x in answer]
    
            
        
    return answer
