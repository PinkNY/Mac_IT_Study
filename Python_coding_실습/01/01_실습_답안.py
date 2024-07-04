def add(a, b):                                              # add라는 함수를 생성하고 a,b변수 추가
    return a + b                                            # a + b 를 add에 대입

# 함수를 호출하고 결과를 출력하세요
c = add(7, 3)                                               # c = 7 + 3 을 진행
print(c)                                                    # 출력: 10




def repeat_string(s, n):                                    # repeat_string 함수를 생성하고 s, n 추가
    return s * n                                            # 

# 함수를 호출하고 결과를 출력하세요
repeated_string = repeat_string("hello", 3)
print(repeated_string)  # 출력: 'hellohellohello'





def sum_all(*args):
    return sum(args)

# 함수를 호출하고 결과를 출력하세요
number = sum_all(10, 20, 30)
print(number)  # 출력: 60

number = sum_all(10, 20, 30, 40, 50)
print(number)  # 출력: 150





def multiply(a, b=1):
    return a * b

# 함수를 호출하고 결과를 출력하세요
result = multiply(7)
print(result)  # 출력: 7

result = multiply(7, 3)
print(result)  # 출력: 21





def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

# 함수를 호출하고 결과를 출력하세요
print_info(name="Alice", age=30)
print_info(age=25, name="Bob")



def add_and_multiply(a, b):
    return a + b, a * b

# 함수를 호출하고 결과를 출력하세요
sum_result, product_result = add_and_multiply(5, 3)
print(f"Sum: {sum_result}, Product: {product_result}")  # 출력: Sum: 8, Product: 15




def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 함수를 호출하고 결과를 출력하세요
print_kwargs(name="Alice", age=30, city="New York")




def mixed_params(a, b, c=0, *args, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# 함수를 호출하고 결과를 출력하세요
mixed_params(1, 2)
mixed_params(1, 2, 3, 4, 5, 6, key1="value1", key2="value2")

