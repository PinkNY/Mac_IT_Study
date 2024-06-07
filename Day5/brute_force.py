# 순열 구하는 함수

# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)

# def permute(data, depth, n, result):
#     if depth == n:
#         print(result)
#         return

#     for i in range(len(data)):
#         if data[i] not in result:
#             result.append(data[i])
#             permute(data, depth + 1, n, result)
#             result.pop()

# data = [1, 2, 3]
# permute(data, 0, len(data), [])


# def permute():
#     pass

# data = [1, 2, 3]
# permute(data)

def permute(data):
    result = []
    stack = [([], data)]

    while stack:
        print(stack)
        perm, items = stack.pop()
        # if not items:
        if len(items) == 0:
            result.append(perm)
        else:
            for i in range(len(items)):
                new_perm = perm + [items[i]]
                new_items = items[:i] + items[i+1:]
                stack.append((new_perm, new_items))

    return result

data = [1, 2, 3]
permutations = permute(data)
for perm in permutations:
    print(perm)


#백준 블랙잭 문제
# 입력
# a, b = map(int, input().split())
# cards = list(map(int, input().split()))

# answer = #결과

# 삼중 반복문 이용. 
n, m = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            three = lst[i] + lst[j] + lst[k]
            if three > m:
                continue
            else:
                nlst.append(three)
print(max(nlst))


# from itertools import combinations

# # 입력 받기
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# # 가능한 모든 조합 중에서 조건을 만족하는 최대합 찾기
# max_sum = 0
# for comb in combinations(lst, 3):
#     curr_sum = sum(comb)
#     if curr_sum <= m:
#         max_sum = max(max_sum, curr_sum)

# print(max_sum)



# 최적화버전
# 입력 받기
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# max_sum = 0

# # 가능한 모든 조합 중에서 조건을 만족하는 최대합 찾기
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             current_sum = lst[i] + lst[j] + lst[k]
#             if current_sum <= m:
#                 max_sum = max(max_sum, current_sum)

# print(max_sum)

## 삼중반복문, GPT추천한 itertoos 이용, 최적화버전 중에서 결국 삼중반복문이 시간은 빠름.

#강사님

n, target = map(int, input().split())
cards = list(map(int, input().split()))
current_max = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            number = cards[i] + cards[j] + cards[k]
            if number <= target and \
                number > current_max:
                    current_max = number
                    
print(current_max)

# 분해합 문제

def digit_sum(n):
    # 자연수 n의 각 자리수의 합을 반환하는 함수
    return sum(map(int, str(n)))

def find_smallest_constructor(n):
    for num in range(1, n + 1):
        if num + digit_sum(num) == n:
            # 분해합이 n과 같은 생성자를 찾았을 때 해당 수 반환
            return num
    # 생성자를 찾지 못한 경우
    return 0

# 자연수 N 입력 받기
N = int(input())

# 가장 작은 생성자 찾기
smallest_constructor = find_smallest_constructor(N)

if smallest_constructor != 0:
    print(smallest_constructor)
else:
    print(0)


############

# 강사님

n = int(input())
printed = False

# 1부터 시작해서 n까지 숫자를 훑어본다.
# 가장 먼저 분해합이 n이 되는 수를 리턴.
for number in range(1, n + 1):
    sum_of_digits = 0
    # for digit in str(number):
    #     sum_of_digits += int(digit)
    sum_of_digits = sum([int(digit) for digit in str(number)])
    if number + sum_of_digits == n:
        printed = True
        print(number)
        break
    
if printed == False:
    print(0)
        
 #####################################
 
 # 수학은 비대면 강의 입니다 문제
 
# 다음 연립방정식에서 x와 y의 값을 계산.
# ax + by = c
# dx + ey = f

# -999 이상 999이하 정수만.
 
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
            print(x,y)

