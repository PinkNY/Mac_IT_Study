# recursive.py

# 팩토리얼

# 5! = 5 x 4 x 3 x 2 x 1
#    = 5 x 4!

def factorial(n):
    if n == 0:
    # 기본 조건
        return 1
    return n * factorial(n -1)
    # 재귀 조건

print(factorial(5))

# 피보나치

# 피보나치 수열 : f(n) = f(n -1) + f(n -2)
# 1, 1, 2, 3, 5, 8, 13, 21, 34(9번째) ...

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:      # fibonacci(1) = 1
        return 1
    return fibonacci(n -1) + fibonacci(n -2)

print (fibonacci(9))

# F(0) = 0 (기본 조건)
# F(1) = 1 (기본 조건)
# F(n) = F(n-1) + F(n-2) (재귀 조건)

# 재귀를 반복문으로 변환
def factorial_iterative(n):
    result = 1
# 1 x 2 x 3 x 4 x 5
# n이 5일때, 1,2,3,4
    for i in range(1, n + 1):
        result *= i
        print(f"{i}번째, result={result}")
    return result


# 피보나치 수열을 반복문으로 변환
def fibonacci_iterative(n):
    a, b = 0, 1
    
    # 0, 1, 2, 3, ..., 8
    for _ in range(n):
        a, b = b, a+b
    return a

def fibonacci_iterative(n):
    a, b = 0, 1
    temp = 0
    
    # 0, 1, 2, 3, ..., 8
    for _ in range(n):
        # temp = b
        # b = a + b
        # a = temp
        print(f"a={a}. b={b}")
        a, b = b, a + b
    return a

# 백준 제출방법
# a, b = map(int, input().split())
# print(a + b)

# 팩토리얼2 문제
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

N = int(input())  # 정수 N 입력
print(factorial(N))  # N! 출력

#  n! = n * (n -1)!
# ! -> factorial(n)
# factorial(n) = n * factorial(n-1)

a = int(input())

def factorial(n):
    if n == 0:
        return 1
    result = n * factorial(n -1)
    return result
print(factorial(a))



# 피보나치수5 문제
n = int(input())

def fibo(n):
    if n == 0:
        result = 0  # 반환하는 값이 없어요!
    elif n == 1 or n == 2:
        result = 1 # 반환하는 값이 없어요!
    else:
        result = fibo(n-1) + fibo(n-2)
        # 반환하는 값이 없으니 fibonacci()는 NoneType가 되고, 이 둘을 더하려 하니 런타임 에러가 발생해요
    return result   
print(fibo(n))


n = int(input())

# 1, 1, 2, 3, 5, 8, 13, 21, 34
# f(n) = f(n -1) + f(n -2)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n -1) + fibo(n-2)

print(fibo(n))