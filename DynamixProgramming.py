counter = 0

# This is fibonnaci without memoization. It is a recursive function that will take a long time to run for large values of n.
def fin(n):
    global counter
    counter += 1
    if n == 0 and n ==1:
        return n 
    
    return fin(n-1) + fin(n-2)


# fibonnaci with memoization. It is a recursive function that will run in linear time for large values of n.
memo = [None] * 100
counter = 0

def fib(n):
    global counter
    counter += 1
    
    if memo[n] is not None:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# Def button up 

counter = 0 
def fin(n):
    fib_list = [0, 1]
    for index in range(2, n + 1):
        counter +=1 
        next_fb = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fb)
    return fib_list[n]