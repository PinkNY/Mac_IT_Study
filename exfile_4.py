# 사용자에게 N1과 N2를 입력받아, N1과 N2의 최대 공약수를 구해 출력.

n1, n2 = map(int, input('Enter two integers: ').split())
print()
min_ = min(n1, n2)
for i in range(1, min_ + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcf = i                                                     # gcf = greatest common factor : 최대공약수

print(f'The greatest common factor of {n1} and {n2} is {gcf}.')
print()