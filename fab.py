def fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fab(n-1) + fab(n-2)

n = 28
print(fab(n))