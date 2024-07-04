### **실습 문제: 파이썬 계산기 모듈 만들기**

### **목표**

# 파이썬으로 기본적인 계산기 모듈을 만들어, 덧셈, 뺄셈, 곱셈, 나눗셈을 수행할 수 있도록 합니다. 또한, 모듈을 이용해 몇 가지 추가 기능을 구현해봅니다.

### **단계별 문제**

# 1. **기본 계산 함수 작성하기**
#     - 덧셈을 수행하는 함수 **`add(a, b)`**를 작성하세요.
#     - 뺄셈을 수행하는 함수 **`subtract(a, b)`**를 작성하세요.
#     - 곱셈을 수행하는 함수 **`multiply(a, b)`**를 작성하세요.
#     - 나눗셈을 수행하는 함수 **`divide(a, b)`**를 작성하세요.
# 2. **예외 처리 추가하기**
#     - **`divide`** 함수에 나누는 수가 0인 경우 오류 메시지를 출력하고 **`None`**을 반환하도록 수정하세요.
# 3. **추가 기능 구현하기**
#     - 제곱을 계산하는 함수 **`power(base, exponent)`**를 작성하세요.
#     - 제곱근을 계산하는 함수 **`sqrt(number)`**를 작성하세요. (이 함수는 음수 입력에 대해 오류 메시지를 출력하고 **`None`**을 반환해야 합니다.)
# 4. **입력 받기 및 결과 출력하기**
#     - 사용자가 원하는 연산과 숫자를 입력받아 계산을 수행하고 결과를 출력하는 **`main()`** 함수를 작성하세요.
#     - **`main()`** 함수는 while 루프를 사용해 사용자가 'exit'를 입력할 때까지 계속해서 계산을 수행합니다.

# main.py

# import calculator

# def main():
#     # 더하기 예시
#     result = calculator.add(10, 5)
#     print(f"10 + 5 = {result}")

#     # 빼기 예시
#     result = calculator.subtract(10, 5)
#     print(f"10 - 5 = {result}")

#     # 곱하기 예시
#     result = calculator.multiply(10, 5)
#     print(f"10 * 5 = {result}")

#     # 나누기 예시
#     result = calculator.divide(10, 5)
#     print(f"10 / 5 = {result}")

#     # 0으로 나누기 예시
#     result = calculator.divide(10, 0)
#     if result is not None:
#         print(f"10 / 0 = {result}")

#     # 거듭제곱 예시
#     result = calculator.power(2, 3)
#     print(f"2^3 = {result}")

#     # 제곱근 예시
#     result = calculator.sqrt(9)
#     print(f"sqrt(9) = {result}")

#     # 음수의 제곱근 예시
#     result = calculator.sqrt(-9)
#     if result is not None:
#         print(f"sqrt(-9) = {result}")

# if __name__ == "__main__":
#     main()
# import calculator

# # calculator.py

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         print("오류: 0으로 나눌 수 없습니다.")
#         return None
#     return a / b

# def power(base, exponent):
#     return base ** exponent

# def sqrt(number):
#     if number < 0:
#         print("오류: 음수의 제곱근을 계산할 수 없습니다.")
#         return None
#     return number ** 0.5

import calculator as cal

a, b = map(int,input().split())
print(f'a는 {a}')
print(f'b는 {b}')


print(cal.add(a,b))
print(cal.subtract(a,b))
print(cal.multiply(a,b))
print(cal.divide(a,b))