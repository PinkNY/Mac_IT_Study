# # 호출 부분
# print(greet("Alice")) # 출력: "Hello, Alice!"
# print(greet("Bob", greeting="Hi")) # 출력: "Hi, Bob!"
# print(greet("Charlie", "Hey", punctuation="!!")) # 출력: "Hey, Charlie!!"

def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice")) # 출력: "Hello, Alice!"
print(greet("Bob", greeting="Hi")) # 출력: "Hi, Bob!"
print(greet("Charlie", "Hey", punctuation="!!")) # 출력: "Hey, Charlie!!"

# 호출 부분
# print(divide(10, 2)) # 출력: 5.0
# print(divide(10, 0)) # 출력: "Error: Division by zero is not allowed."

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide(10, 2)) # 출력: 5.0
print(divide(10, 0)) # 출력: "Error: Division by zero is not allowed."


# 호출 부분
# from mymath import add, multiply

# print(add(3, 5)) # 출력: 8
# print(multiply(3, 5)) # 출력: 15

from mymath import add, multiply

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

print(add(3, 5)) # 출력: 8
print(multiply(3, 5)) # 출력: 15

# 호출 부분
# class Animal:
#     pass
    
# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# animals = [Dog("렉스"), Cat("위스커스"), Animal("제네릭")]
# for animal in animals:
#     print(f"{animal.name}(이)가 {animal.speak()}")
# 출력:
# 렉스(이)가 멍멍!
# 위스커스(이)가 야옹!
# 제너릭(이)가 어떤 소리를 냅니다

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return("어떤 소리를 냅니다.")
        
class Dog(Animal):
    def speak(self):
        return "멍멍!"
    
class Cat(Animal):
    def speak(self):
        return "야옹!"
    
animals = [Dog("렉스"), Cat("위스커스"), Animal("제네릭")]
for animal in animals:
    print(f"{animal.name}(이)가 {animal.speak()}")
# 출력:
# 렉스(이)가 멍멍!
# 위스커스(이)가 야옹!
# 제너릭(이)가 어떤 소리를 냅니다
