# 사용자에게 자연수 2개 N1, N2를 입력 받는다.
# 자연수 N1 N2 사이에 있는 자연수들의 합계를 구해서 출력한다.
'''
n1, n2 = map(int, input('Enter two positive integers: ').split())
c = min(n1,n2)
d = max(n1,n2)
answer = 0

for i in range(c,d+1):
    answer +=i

print('result = ', answer)
'''
'''
n1, n2 = map(int, input('Enter two positive integers: ').split())
result = 0
if n1 < n2:
    for i in range(n1, n2 + 1):
        result += i
    else:
        for i in range(n2, n1 +1):
            result += i
'''
'''
n1, n2 = map(int, input('Enter two positive integers: ').split())
if n1 < n2:
    result = sum(range(n1, n2 + 1))
else:
    result = sum(range(n2, n1 + 1))

print('result =', result)
'''
'''
# max, min함수 이용하는 방법
n1, n2 = map(int, input('Enter two positive integers: ').split())
max_, min_ = n2, n1

if n1 > n2:
    max_, min_ = n1, n2
result = sum(range(min_, max_ +1))
print('result =', result)
'''
# max_, min_ = max(n1, n2), min(n1, n2)
# result = sum(range(min_, max_ +1))
# print('result =', result)
'''
# range 함수의 세 번째 인자를 지정할 변수
n1, n2 = map(int, input('Enter two positive integers: ').split())
step = 1
if n1 > n2:
    step = -1
result = sum(range(n1, n2 + step, step))
print('result =', result)
'''

