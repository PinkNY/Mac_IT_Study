'''
# 사용자에게 정수 하나 입력 받아서 양수인지 음수인지 0인지 확인해서 출력
num = int(input('Enter an integer: '))
print()
if num > 0:
    print(num, "is a positive integer")
elif num < 0:
    print(num, "is a negative integer")
else:
    print(num, "is zero")
print()

# 사용자에게 자연수 두개 입력 받아서 N1이 N2의 약수인지 배수인지 약수도 배수도 아닌지 확인해서 출력
n1, n2 = map(int, input('Enter two integers: ').split())
print()
if n2 % n1 == 0:
    print(f"{n1} is a factor of {n2}.")
elif n1 % n2 == 0:
    print(f"{n1} is a factor of {n2}.")
else:
    print(f"{n1} is neither a factor of {n2} nor a multiple.")
print()

# 사용자에게 국어 영어 수학 점수를 입력 받아 평균값 구하고 등급과 평균을 출력
Korea = int(input('Enter your korea score: '))
English = int(input('Enter your english score: '))
Math = int(input('Enter your math score: '))

average = (Korea + English + Math) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Average: {average:.2f}')
print('Grade:', grade)

'''

#

salary = int(input('Enter your salary: '))
print()
if salary >= 8000000:
    tax_rate = 0.3
elif salary >= 5000000:
    tax_rate = 0.25
elif salary >= 2000000:
    tax_rate = 0.2
else:
    tax_rate = 0.15
incom_tax = int(salary * tax_rate)
amount_received = salary - incom_tax
print(f'Income tax: {incom_tax}')
print(f'Amount received: {amount_received}')
print()
