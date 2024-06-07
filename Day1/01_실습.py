# f(x) = x

def f1(x):
    return x

print(f1(5))

# f(x) = 2x + 1

def f2(x):
    return 2 * x + 1

print(f2(5))

# f(x) = x^2 + 2x + 1

def f3(x):
    return x ** 2 + 2 * x + 1

print(f3(5))


def mul(*values):
    result = 1
    for value in values:
        #result = result * value // 위 아래 두가지 활용 가능.
        result *= value
    return result

print(mul(5, 7, 9, 10))
# 3150

##############################

def add(a, b):
    # 여기에 코드를 작성하세요
    return a+b

# 함수를 호출하고 결과를 출력하세요
c = add(7, 3)
c # 10



def repeat_string(s, n):
    return s * n

# 함수를 호출하고 결과를 출력하세요
repeated_string = repeat_string("hello", 3)
print(repeated_string)  # 출력: 'hellohellohello'



def sum_all(*args):
    # 여기에 코드를 작성하세요
    return sum(args)
        

# 함수를 호출하고 결과를 출력하세요
number = sum_all(10, 20, 30)
number # 60

number = sum_all(10, 20, 30, 40, 50)
number # 150



def multiply(a, b=1):
    # 여기에 코드를 작성하세요
    return a * b

# 함수를 호출하고 결과를 출력하세요
result = multiply(7)
print(result)  # 출력: 7

result = multiply(7, 3)
print(result)  # 출력: 21




def print_info(name, age):
    # 이름과 나이를 출력하는 코드를 작성하세요
    print(f"Name: {name}, Age: {age}")

# 함수를 호출하고 결과를 출력하세요
print_info(name="Alice", age=30)
print_info(age=25, name="Bob")




def add_and_multiply(a,b):
    # 두 숫자의 합과 곱을 반환하는 코드를 작성하세요
    return a + b, a * b

# 함수를 호출하고 결과를 출력하세요
sum_result, product_result = add_and_multiply(5, 3)
print(f"Sum: {sum_result}, Product: {product_result}")  # 출력: Sum: 8, Product: 15




def print_kwargs(**kwargs):
    # 키워드 인자의 값을 출력하는 코드를 작성하세요
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 함수를 호출하고 결과를 출력하세요
print_kwargs(name="Alice", age=30, city="New York")





def mixed_params(a, b, c=0, *args, **kwargs):
    # 필수 매개변수, 기본 매개변수, 가변 매개변수, 키워드 가변 매개변수를 출력하는 코드를 작성하세요
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# 함수를 호출하고 결과를 출력하세요
mixed_params(1, 2)
mixed_params(1, 2, 3, 4, 5, 6, key1="value1", key2="value2")



