# The Fibonacci sequence starts like this: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 and so on forever. Each number is the sum of the two numbers that precede it

# find the nth Term of Fibonacci sequence 

# def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 11):
#     print(n, ":", fibonacci(n))
    
# memoization

# fibonacci_cache = {}

# def fibonacci(n):
# # If we have cached the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]

#     # Compute the Nth term
#     if n == 1:
#         value=1
#     elif n==2:
#         value=1
#     elif n>2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#     # catch the value and return it 
#     fibonacci_cache[n] = value
#     return value

# for n in range(1, 100001):
#     print(n, ":", fibonacci(n))

# -----------------------------------



from functools import lru_cache

@lru_cache(maxsize=1000)

def fibonacci(n):
    # for data validation we can use if clause with condition
    
    if type(n)!=int:
        raise TypeError('n must be an integer')
    
    if n<1:
        raise ValueError('Must be greater than 1')
    
    
    if n == 1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
        
for n in range(1,501):
    print(n,':',fibonacci(n))
