'''
radius = int(input("Enter a raius of the circle" ))
print()
pi = 3.141592
area = pi * radius ** 2
circumference = 2 * pi * radius
print('pi =', pi)
print("radius of the circle =", radius)
print(f'area of the circle = {area:.3f}')
print(f'circumferece of the circle = {circumference:.3f}')
'''
n1, n2 = map(int, input("Enter two integers: ").split())
print()
quotient = n1 // n2
remainder = n1 % n2
print("Quotient = ", quotient)
print("Remainder = ", remainder)