
def factorial(n):
    fact = 1
    for number in reversed(range(1,n+1)):
        fact*=number
    return fact
        
n = 5
print(factorial(n=n))