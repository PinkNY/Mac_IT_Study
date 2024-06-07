'''
num = int(input("Enter an integer: "))                      # 정수 입력하라
if num > 40:                                                # 만약 정수가 40보다 크면
    print("Hello World!")                                   # Hello World! 를 출력하라


num = int(input("Enter an integer: "))                      # 정수를 입력하라
print()                                                     # 만약 정수가 20보다 크고 40보다 작다면
if 20<num< 40:                  
    print("Do your best!")                                  # Do your best! 를 출력하라
print()


num = int(input("Enter an integer: "))
print()
if num < 20 or num > 40:                           
    print("Dream comes ture!")
print()


num = int(input("Enter an integer: "))
print()
if num < 10 or num > 40:
    print("Hello World!")
else:
    print("Hello Python!")
print()
'''

num = int(input("Enter a positive integer: "))
if num % 2 == 1:
    print("Odd number")                         # print('{} is an odd number'.format(num))
else:
    print("Even number")                        # print(num, 'is an even number')
print()
