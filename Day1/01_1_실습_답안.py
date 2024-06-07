def add(a, b):
    return a + b

# 함수를 호출하고 결과를 출력하세요
print(add(5, 3))  # 출력: 8



def repeat_string(s):
    return s * 3

# 함수를 호출하고 결과를 출력하세요
print(repeat_string("hello"))  # 출력: hellohellohello


def add_and_multiply(a, b):
    return a + b, a * b

# 함수를 호출하고 결과를 출력하세요
sum_result, product_result = add_and_multiply(5, 3)
print(f"Sum: {sum_result}, Product: {product_result}")  # 출력: Sum: 8, Product: 15



def longest_string(strings):
    return max(strings, key=len)

# 함수를 호출하고 결과를 출력하세요
print(longest_string(["apple", "banana", "cherry", "date"]))  # 출력: banana


def sum_all(*args):
    return sum(args)

# 함수를 호출하고 결과를 출력하세요
print(sum_all(1, 2, 3, 4, 5))  # 출력: 15
print(sum_all(10, 20, 30))  # 출력: 60



def concatenate_all(*args):
    return ' '.join(args)

# 함수를 호출하고 결과를 출력하세요
print(concatenate_all("Hello", "world", "this", "is", "Python"))  # 출력: Hello world this is Python



def multiply(a, b=1):
    return a * b

# 함수를 호출하고 결과를 출력하세요
print(multiply(7))  # 출력: 7
print(multiply(7, 3))  # 출력: 21


def repeat_string(s, n=1):
    return s * n

# 함수를 호출하고 결과를 출력하세요
print(repeat_string("hello"))  # 출력: hello
print(repeat_string("hello", 3))  # 출력: hellohellohello



def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

# 함수를 호출하고 결과를 출력하세요
print_info(name="Alice", age=30)
print_info(age=25, name="Bob")



def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 함수를 호출하고 결과를 출력하세요
print_kwargs(name="Alice", age=30, city="New York")