'''

while True:
    num = int(input('Enter minutes: '))

    if num == 0:
        break
    hours = num // 60
    minutes = num % 60

    if hours == 1:
        str_hours = f'{hours} hours'
    elif hours > 1:
        str_hours = f'{hours} hours'

    if minutes == 1:
        str_minutes = f'{minutes} minute'
    elif minutes > 1:
        str_minutes = f'{minutes} minutes'
    print(f'{num} minutes = {str_hours}{str_minutes}')
    print()

print('Good Bye!')

'''
'''
# 사용자에게 자연수 N1, N2를 입력 받는다.
# 자연수 N1, N2 사이에 있는 자연수들 중에서 1의 자리가 3이 아닌 자연수를 출력
# N1과 N2는 포함하지 않는다.

n1, n2 = map(int, input('Enter two positive integers: ').split())
if n1 > n2:
    n1, n2 = n2, n1
for i in range(n1 + 1, n2):
    if i % 10 != 3:
        print(i, end=" ")
print()

# break와 continue 문은 반드시 필요한 경우에만 사용하는게 좋다.

'''



