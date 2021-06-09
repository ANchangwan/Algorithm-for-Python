def gcd(x,y):
    return y if x == 0 else gcd(y%x,x)

def solustinos(w,h):
    return w*h - (w + h - gcd(w,h))

print(solustinos(8,12))