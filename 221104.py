'''
# 리스트 numbers에는 1,2,3,4 가 여러개 저장 됨
# 리스트 numbers에 저장되어 있는 1,2,3,4 의 개수만큼 "*"을 찍어 그래프를 그림


numbers = [2, 3, 1, 3, 1, 3, 1, 4, 2, 3, 1, 3]
for i in range(1, 5):
    print(i, '*' * numbers.count(i))
print()

'''


'''
# 사용자가 숫자 0을 입력할 때까지, 또는 최대 30개의 정수를 입력할 때까지 정수들을 입력
# 이때 0은 사용자가 입력한 정수에 포함하지 않는다.
# 사용자가 입력한 정수들의 평균을 구해 출력한다.
# 사용자가 입력한 정수들 중에서 평균보다 큰 정수들의 백분율을 구해 출력
numbers = list()
for i in range(30):
    num = int(input('Enter an integer: '))
    if num == 0: break
    numbers.append(num)
average = sum(numbers) / len(numbers)
print()

print()
'''

# 사용자에게 자연수를 입력 받는다
# 자연수 N의 1의 자리, 10의 자리 , 100의 자리 등을 출력.



numbers = list()
num = int(input('Enter an integer: '))
numbers.append(num)
print()
print(f"1's digit = {numbers[-1]}")
print(f"10's digit = {numbers[-2]}")
print(f"100's digit = {numbers[-3]}")
print(f"1000's digit = {numbers[-4]}")
print(f"10000's digit = {numbers[-5]}")
print()


