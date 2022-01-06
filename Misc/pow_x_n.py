
def pow(x, n):
    
    if x == 0 or x == 1:
        return x
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1/x
    
    half = pow(x, n//2)

    if n&1:
        return x*half*half
    else:
        return half*half