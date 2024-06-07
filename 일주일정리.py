# 함수 정의, 호출, 결과를 출력 하는 방법들을 배움.
# 매개변수, 리턴값, 가변 매개변수, 기본 매개변수, 키워드 매개변수에 대해 배움.
# 리스트, 튜플, 콜백, 람다, 고차 with등 다양한 함수를 배움.

# def add_and_mutiply(a,b):
#   return a + b, a * b
# 두 숫자의 합과 곱을 튜플로 반환.

# def apply_callback(a, b, callback):
#   return callback(a, b)
# 콜백 함수를 두 숫자에 적용한 결과를 반환.

# def add(a,b):
#   return a + b
# 콜백 함수 예시

# result = apply_callback(5,3,add)
# print(result)
# 함수를 호출하고 결과를 출력.

# sum_lambda = lambda a, b: a + b
# 두 숫자의 합을 반환하는 람다 함수

# result = sum_lambda(5,3)
# print(result)
# 람다 함수를 호출하고 결과를 출력.

# def higher_order_function(a, b, func):
#   return func(a,b)
# 함수를 두 숫자에 적용한 결과를 반환.

############
# 추가로 정리할 내용

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 첫 번째 행의 첫 번째 요소 접근
print(matrix[0][0])  # 출력: 1

# 두 번째 행의 세 번째 요소 접근
print(matrix[1][2])  # 출력: 6

# 2차원 배열의 요소에 접근하려면 두 개의 인덱스를 사용합니다.
# 하나는 행(row)을, 다른 하나는 열(column)을 나타냅니다.

# 첫 번째 행의 두 번째 요소 수정
matrix[0][1] = 20
print(matrix[0][1])  # 출력: 20

# 세 번째 행의 첫 번째 요소 수정
matrix[2][0] = 70
print(matrix[2][0])  # 출력: 70

# 0으로 초기화된 3x3 배열
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)  # 출력: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 2차원 배열의 모든 요소를 출력
# 2차원 배열의 순회.
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()


# 2차원 배열의 합계 계산
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element

print(total_sum)  # 출력: 45

# 두 번째 행의 합계
row_sum = sum(matrix[1])
print(row_sum)  # 출력: 15

# 세 번째 열의 합계
col_sum = sum(row[2] for row in matrix)
print(col_sum)  # 출력: 18


# 2차원 배열을 함수로 처리
def double_elements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= 2
    return matrix

# 예제 배열
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 함수 호출
doubled_matrix = double_elements(matrix)
print(doubled_matrix)
# 출력: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]







