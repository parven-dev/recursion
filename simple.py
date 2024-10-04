
def factorial(n):
    fact = 1
    for num in reversed(range(1,n+1)):
        fact*=num
    return fact
        
n = 5
print(factorial(n=n))