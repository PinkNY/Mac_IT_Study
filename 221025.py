'''
# 1부터 20까지 정수들 중에서 짝수들을 출력.
for i in range(2,21,2):
    print('i =', i)

# for 구문과 조건문을 이용해서 출력.
for i in range(1, 21):
    if i % 2 == 0:
        print('i =', i)
'''
'''
# 1부터 50까지 정수들 중에서 5의 배수를 출력.
for i in range(5, 51, 5):
    print('i =', i)

# for 구문과 조건문을 이용해서 출력.
for i in range(1, 51):
    if i % 5 == 0:
        print('i =', i)
'''
'''
# 1부터 100까지의 정수들 중에서 3의 배수이면서 5의 배수인 정수를 출력
for i in range(1, 101):                 # 1부터 100까지의 정수를 확인
    if i % 3 == 0 and i % 5 == 0:       # 그중에서 3의 배수이면서 5의 배수인 정수들만 출력
        print('i =', i)

for i in range(1, 101):                 # 1부터 100까지의 정수를 확인
    if i % 15 == 0:                     # 그중에서 15의 배수인 정수들만 출력
        print('i =', i)

for i in range(15, 101, 15):
    print('i =', i)
'''
'''
# 사용자가 입력한 정수 만큼 문자열 출력
num = int(input('Enter a positive integer : '))
print()
for i in range(1, num + 1):
    print(f'{i}. Hello World!')

num = int(input('Enter a positive integer : '))
print()
for i in range(num):
    print(f'{i + 1}. Hello World!')
'''

# 1부터 100까지의 자연수들의 합계를 구해 출력.

