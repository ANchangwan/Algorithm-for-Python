def solution(A,B,K):
  num1 = A // K
  num2 = B // K
  result = 0
  if A % K == 0 and A!=0:
    result = (num2 - num1) + 1
  else:
    result = (num2 - num1)
    
  if A == 0:
    result += 1
    
  return result
  
