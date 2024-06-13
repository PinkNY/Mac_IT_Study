'''
# 리스트 scores의 모든 요소들의 합계와 평균을 구해 출력

scores = [88, 92, 76, 64, 86, 96]
i = 0
result = 0

while result <= scores:
    i += scores.index
    result += scores.index
print('sum =', result)
print('average =', result // scores)
'''

'''
# 사용자에게 정수 10개를 입력 받는다.
# 사용자가 입력한 정수들의 합계와 평균을 구해 출력한다.

LENGTH = 10
result = 0

for i in range(LENGTH):
    num = int(input('Enter an integer: '))
    result += num

average = result / LENGTH

print('sum = ', result)
print(f'average = {average:.1f}')
'''

'''
LENGTH = 10
numbers = []

for i in range(LENGTH):
    num = int(input('Enter an integer: '))
    numbers.append(num)

result = sum(numbers)

average = result / LENGTH

print('sum = ', result)
print(f'average = {average:.1f}')
'''



# 사용자에게 정수 10개를 입력 받는다.
# 사용자가 입력한 정수들 중에서 최댓값과 최솟값을 구해 출력

LENGTH = 10
numbers = []

for i in range(LENGTH):
    num = int(input('Enter an integer: '))
    numbers.append(num)
print('Maximum value = ', max(numbers))
print('Minimum value = ', min(numbers))
print()




