# solution 1
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0]*(n+1)  
f(n)              
fibo = [str(i) for i in fibo]   
ans = ",".join(fibo)    
print(ans)

# solution 2
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1)+fibonacci(n-2)

def print_fiblist(n):
    fib_list = [(str(fibonacci(i))) for i in range(0, n+1)]
    return print(",".join(fib_list))
n = int(input())
print_fiblist(n)

