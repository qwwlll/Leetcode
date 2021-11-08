###fib
def fib (n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a 

print(fib(1000))



def fib_res(n):
    if n == 1 or n == 2:

        return 1
  
    return fib_res(n-1)+fib_res(n-2)

print (fib_res(1))