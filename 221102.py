'''
numbers = [4, 17, 32, 3, 8, 13, 41, 27, 16, 1]
for i in range(len(numbers)):
    print(f'numbers[{i}] = {numbers[i]}')
print()
'''


'''
numbers = [4, 17, 32, 3, 8, 13, 41, 27, 16, 1]
while i < len(numbers):
    print(f'numbers[{i}] = {numbers[i]}')
print()
'''


'''
numbers = [4, 17, 32, 3, 8, 13, 41, 27, 16, 1]
for index, item in enumerate(numbers):
    print(f'numbers[{index}] = {item}')

'''


'''
numbers = [4, 17, 32, 3, 8, 13, 41, 27, 16, 1]
for item in numbers:
    print('item =', item)
print()
'''

'''
hello = 'Hello World!'
for ch in 'Hello World!':
    print('ch = ', ch)
print()
'''


'''
scores = {'korean':86, 'math':96, 'english':68}
for key in scores:
    print('{}: {}'.format(key.title(), scores[key]))
print()
'''


'''
for key in scores.keys():
    print(f'{key.title()}: {scores.get(key)}')
print()
'''


'''
scores = {'korean':86, 'math':96, 'english':68}
for value in scores.values():
    print('value = ', value)
print()
'''


'''

for key, value in scores.items():
    print(f'{key.title()}: {value}')
print()

'''


'''
# 리스트 numbers의 요소들을 5만큼 크게 출력

numbers = [4, 17, 32, 3, 8, 13, 41, 27, 16, 1]
for item in numbers:
    print(item + 5)
print()

'''


'''
# 리스트 scores에서 80보다 큰 요소들의 인덱스와 값을 차례대로 출력
scores = [88, 92, 76, 64, 80, 96, 84, 72, 68, 100]
for i in range(len(scores)):
    if scores[i] > 80:
        print(f'scores[{i}] = {scores[i]}')
print()


scores = [88, 92, 76, 64, 80, 96, 84, 72, 68, 100]
for index, item in enumerate(scores):
    if item > 80:
        print(f'scores[{index}] = {item}')
print()

'''

# 리스트 numbers의 요소들 중에서 짝수 번째 요소들만 차례대로 출력.
numbers = [4, 17, 32, 3, 8, 13, 41, 27, 16, 1]
for i in range(len(numbers)):
    if i % 2 == 1:
        print(numbers[i])
