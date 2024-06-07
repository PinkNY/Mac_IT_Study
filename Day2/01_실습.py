### **문제 1: 튜플을 사용하는 함수**

# 튜플을 반환하는 함수를 정의하라. 이 함수는 두 개의 숫자를 입력받아, 그 합과 곱을 튜플로 반환한다. 그리고 이 함수를 호출하여 결과를 출력하라.

def add_and_multiply(a,b):
    return a+b, a*b
    # 두 숫자의 합과 곱을 튜플로 반환하는 코드를 작성하세요

# 함수를 호출하고 결과를 출력하세요
result = add_and_multiply(5, 3)
print(result)  # 출력: (8, 15)

### **문제 2: 콜백 함수**

# 콜백 함수를 사용하는 함수를 정의하라. 이 함수는 두 개의 숫자와 하나의 콜백 함수를 입력받아,
# 콜백 함수를 두 숫자에 적용한 결과를 반환한다. 그리고 이 함수를 호출하여 결과를 출력하라.

def apply_callback(a,b, callback):
    return callback(a,b)
    # 콜백 함수를 두 숫자에 적용한 결과를 반환하는 코드를 작성하세요

# 예시 콜백 함수
def add(a, b):
    return a + b

# 함수를 호출하고 결과를 출력하세요
result = apply_callback(5, 3, add)
print(result)  # 출력: 8

### **문제 3: 람다 함수**

# 람다 함수를 사용하는 예제를 작성하라. 두 개의 숫자를 입력받아, 그 합을 반환하는 람다 함수를 정의하고 이를 호출하여 결과를 출력하라.

sum_lambda = lambda a, b: a+b
# 두 숫자의 합을 반환하는 람다 함수를 작성하세요

# 람다 함수를 호출하고 결과를 출력하세요
result = sum_lambda(5, 3)
print(result)  # 출력: 8

### **문제 4: 고차 함수**

# 고차 함수를 사용하는 예제를 작성하라. 두 개의 숫자와 하나의 함수를 입력받아,
# 이 함수를 두 숫자에 적용한 결과를 반환하는 고차 함수를 정의하고 이를 호출하여 결과를 출력하라.

def higher_order_function(a,b,func):
    return func(a,b)
    # 함수를 두 숫자에 적용한 결과를 반환하는 코드를 작성하세요

# 예시 함수
def multiply(a, b):
    return a * b

# 고차 함수를 호출하고 결과를 출력하세요
result = higher_order_function(5, 3, multiply)
print(result)  # 출력: 15

### **문제 5: with 구문**

# with 구문을 사용하는 예제를 작성하라. 파일을 열고, 파일에 문자열을 쓰는 함수를 정의하고 이를 호출하여 결과를 출력하라.

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    # 파일에 문자열을 쓰는 코드를 작성하세요

# 함수를 호출하고 결과를 출력하세요
write_to_file('example.txt', 'Hello, world!')


#####################################################################

numbers = [1, 2, 3, 4, 5, 6]

# print("::".join(str(numbers)))

# 1. 반복문

for i, number in enumerate(numbers):
    numbers[i] = str(number)

print("::".join(numbers))

# 2. 고차함수

numbers = map(str, numbers)

print("::".join(numbers))

# 3. 리스트컨프리헨션

numbers = [str(number) for number in numbers]

print("::".join(numbers))

#########################################################################

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("# 3이상, 7미만 추출하기")
print(list(filter(lambda x: x >= 3 and x < 7, numbers)))
print()

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x: x ** 2 < 50, numbers)))












