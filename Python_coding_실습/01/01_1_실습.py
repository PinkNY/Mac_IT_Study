# ### **1. 함수 정의와 호출 (10분)**

# **문제 1:**

# - 두 숫자를 입력받아 그 합을 반환하는 함수를 작성하라.

def add(a,b):
    return a+b
c = add(10, 4)

# - 함수를 호출하여 결과를 출력하라.

print(c)

# **문제 2:**

# - 문자열을 입력받아 해당 문자열을 3번 반복하여 반환하는 함수를 작성하라.

def repeat_string(s,n):
    return s * n
repeated_string = repeat_string("Thank", 3)

# - 함수를 호출하여 결과를 출력하라.

print(repeated_string)

# ### **2. 매개변수와 리턴값 (10분)**

# **문제 3:**

# - 두 숫자를 입력받아 두 숫자의 합과 곱을 반환하는 함수를 작성하라.

def add_and_multiply(a, b):
    return a + b, a * b

sum_result, product_result = add_and_multiply(5, 3)

# - 함수를 호출하여 결과를 출력하라.

print(f"Sum: {sum_result}, Product: {product_result}")

# **문제 4:**

# - 주어진 문자열 리스트에서 가장 긴 문자열을 반환하는 함수를 작성하라.

my_list = ["asd", "eijedk", "dkfnldfjakdj"]


# - 함수를 호출하여 결과를 출력하라.


# ### **3. 가변 매개변수 (10분)**

# **문제 5:**

# - 여러 개의 숫자를 입력받아 그 합을 반환하는 함수를 작성하라.

def add(a,b,c):
    return a + b + c

number = add(8 + 29 + 13)

# - 함수를 호출하여 결과를 출력하라.

print(number)

# **문제 6:**

# - 여러 개의 문자열을 입력받아 모든 문자열을 공백으로 연결한 문자열을 반환하는 함수를 작성하라.


# - 함수를 호출하여 결과를 출력하라.


# ### **4. 기본 매개변수 (10분)**

# **문제 7:**

# - 두 숫자를 입력받아, 두 번째 숫자가 주어지지 않으면 기본값으로 1을 사용하여 곱셈을 수행하는 함수를 작성하라.
# - 함수를 호출하여 결과를 출력하라.

# **문제 8:**

# - 문자열과 반복 횟수를 입력받아, 반복 횟수가 주어지지 않으면 기본값으로 1을 사용하여 문자열을 반복하는 함수를 작성하라.
# - 함수를 호출하여 결과를 출력하라.


# ### **5. 키워드 매개변수 (10분)**

# **문제 9:**

# - 키워드 매개변수를 사용하여 이름과 나이를 출력하는 함수를 작성하라.
# - 함수를 호출하여 결과를 출력하라.

# **문제 10:**

# - 키워드 가변 매개변수를 사용하여 여러 개의 키워드 인자를 받아 각 인자의 값을 출력하는 함수를 작성하라.
# - 함수를 호출하여 결과를 출력하라.