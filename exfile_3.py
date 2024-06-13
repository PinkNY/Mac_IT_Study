# 사용자에게 자연수 N1과 N2를 입력 받는다.
# 1부터 N1까지의 자연수들 중에서 N2의 배수들을 출력하고, 그 배수들의 개수를 구해 출력
# 1<=n<=N1
n1, n2 = map(int, input('Enter two positive integers: ').split())
multiples = list(range(n2, n1 + 1, n2))
print(f'Multiples of {n2} =', *multiples)
print('Number of multiples =', len(multiples))
print()
