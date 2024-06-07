'''
n1, n2 = map(int, input('Enter two integers: ').split())
print(f'n1 = {n1}, n2 = {n2}')
tmp = n1                                    # 임시 변수(temporary variable) 사용 가능.
n1 = n2
n2 = tmp
print(f'n1 = {n1}, n2 = {n2}')              # n1 = 20 n2 = 10
n1, n2 = n2, n1
print(f'n1 = {n1}, n2 = {n2}')              # n1 = 10 n2 = 20
'''
