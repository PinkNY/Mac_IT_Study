# 표준 입력(standard input)
# -> 컴퓨터 시스템의 기본 입력 장치

# input 함수를 이용해 표준 입력을 통해 사용자에게 값을 입력
# -> 사용자가 키보드를 이용해 값을 입력하고 엔터 키를 입력할 때까지 사용자 입력을 대기.
# input()

value = input()

print('value = ', value)
print()

# 프람프트 메시지(prompt message)를 출력해서, 사용자가 어떤 동작을 해야 하는지 알림.
# 출력할 프람프트 메시지는 input 함수에 저장한다.

value = input('Enter an integer: ')

print('value =', value)

# print('value + 5 =', value + 5)                           # WRONG #
# print('value + 5 =', '10' + 5)
# input 함수를 이용해 값을 입력 받으면 그 값은 문자열(string)이다.
# type 함수를 이용해, 변수 value의 자료형 확인
print('type(value) =', type(value))

# input 함수를 이용해 받은 값은 항상 문자열(string)이다. 따라서 프로그램에서 필요한 자료형으로 변환 후 사용.
value = int(value)
# value = int('10')
# value = 10
print('value + 5 =', value + 5)
print()

# 한 문장에서 input 함수와 변환 함수를 같이 사용할 수 있다.
# value = input('Enter an integer: ')
# value = int(value)
value = int(input('Enter an integer: '))
# input 함수를 이용해 표준 입력에서 읽어온 문자열을 int 변환 함수를 이용해 정수로 변환 후 변수 value에 대입.
print('value + 10 =', value + 10)
print()

n1, n2 = map(int, input('Enter two integers: ').split())
# -> n1, n2 = map(int, '10 20'.split())
# -> n1, n2 = map(int, ('10', '20'))
# -> n1, n2 = (int('10'), int('20'))
# -> n1, n2 = (10, 20)
print('n1 + n2 =', n1 + n2)
print()

n1, n2, n3 = map(int, input('Enter three integers: ').split())
print(f'n1 = {n1}, n2 = {n2}, n3 = {n3}')

# 사용자에게 원의 반지름을 정수로 입력 받는다
radius = int(input("Enter a raius of the circle" ))
print()

# 원주율을 나타내는 변수
pi = 3.141592

# 반지름이 radius인 원의 면적과 둘레를 계산
area = pi * radius ** 2
circumference = 2 * pi * radius

# 출력
print('pi =', pi)
print("radius of the circle =", radius)
print(f'area of the circle = {area:.3f}')
print(f'circumferece of the circle = {circumference:.3f}')
# print('area of the circle = {:.3f}'.format(area))
# print('circumferece of the circle = {:.3f}'.format(circumference))
# 출력 한번에 하고 싶다면
print(f'''pi = {pi}
radius of the circle = {radius}
area of the circle = {area:.3f}
circumference of the circle = {circumference:.3f}
''')
#
# 사용자에게 정수 2개, n1 과 n2를 입력 받아, n1을 n2로 나눈 몫과 나머지를 구해 출력

# 사용자 입력
# '10 3' -> ('10', '3') -> (10, 3)
n1, n2 = map(int, input('Enter two integers: ').split())
print()

# 변수 n1을 n2로 나눈 몫과 나머지를 계산
quotient = n1 // n2
remainder = n1 % n2

# 출력
print("Quotient = ", quotient)
print("Remainder = ", remainder)
print()
