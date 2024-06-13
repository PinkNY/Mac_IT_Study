# 사용자에게 자연수 N을 입력
# 1부터 1씩 증가하는 자연수를 차례대로 더함
# 지금까지의 합계가 사용자가 입력한 N 보다 커지면 지금까지의 합계와 마지막으로 더한 자연수를 출력
'''
num = int(input('Enter a positive integer : '))
result = 0                      # 1부터 1씩 증가하는 자연수들의 합계를 저장할 변수
i = 0                           # 1부터 1씩 증가하는 자연수를 표현하는 인덱스 변수
while result <= num:            # 합계가 입력값보다 작거나 같을 동안 반복수행
    i += 1                      # i에 1씩 누적 더하고 대입
    result += i                 # result에 i의 값을 누적해서 더하고 대입

print('sum =', result)
print('number =', i)
'''

# 사용자가 정수 0을 입력 할때까지 정수를 입력 받는다.
# 사용자가 입력한 정수들의 합을 구해서 출력
'''
result = 0
while True:
    num = int(input('Enter an integer : '))
    if num == 0:
        break
    result += num
print('Enter an integer : ', result)
'''

# 사용자가 숫자 0을 입력 할때까지 M "분(minute)"을 입력 받는다.
# M분을 "시간(hour)"과 "분"으로 나눠 출력한다.
# 이때 단수(Singular)와 복수(Plural)를 따져서 출력한다.


M = 0
H = 0
result = 0
num = int(input('Enter minute : '))
while num > 3600:
    H += 1
    print(f'{1} hours'(H))
while num > 60:
    M += 1
    print(f'{1} hour {2} minutes'(H,M))
    break




