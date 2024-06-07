# class Calculator:
 
#     def __init__(self,num1, num2):
#         self.num1 = num1
#         self.num2 = num2
 
#     def sum(self):
#         return self.num1 + self.num2
 
#     def mul(self):
#         return self.num1 * self.num2
 
#     def sub(self):
#         return self.num1 - self.num2
 
#     def div(self):
#         return self.num1 / self.num2
    
# def main():
#     calc = Calculator(int(input("첫번째 수"))
#                       ,int(input("두번째 수")))
#     print("{} + {} = {}"
#           .format(calc.num1
#                   , calc.num2
#                   , calc.sum()))
#     print("{} - {} = {}"
#           .format(calc.num1
#                   , calc.num2
#                   , calc.sub()))
#     print("{} * {} = {}"
#           .format(calc.num1
#                   , calc.num2
#                   , calc.mul()))
#     print("{} / {} = {}"
#           .format(calc.num1
#                   , calc.num2
#                   , calc.div()))
 
# if __name__ == '__main__':
#     main()


def add(a,b):
    return a + b
 
def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return
    return a/b

def power(a, b):
    return a ** b

def sqrt(number):
    if number < 0:
        print("음수의 제곱근을 취할 수 없다.")
        return
    return number ** 0.5