# 시간 복잡도 - 빅 오(Big-O) 표기법

# O(1) - 상수 시간 복잡도
# 입력 크기와 상관없이 일정한 시간이 걸리는 알고리즘

# 예시: 배열의 첫 번째 원소를 출력하는 함수
def print_first_element(arr):
    print(arr[0])

# 시간 복잡도: O(1)

#########################################################

# O(log n) - 로그 시간 복잡도
# 입력 크기가 커질수록 실행 시간이 로그 형태로 증가하는 알고리즘입니다.
# 이진 탐색 알고리즘이 대표적입니다.

# 예시: 이진 탐색
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 시간 복잡도: O(log n)

#########################################################

# O(n) - 선형 시간 복잡도
# 입력 크기에 비례하여 실행 시간이 증가하는 알고리즘입니다.

# 예시: 배열의 모든 원소를 출력하는 함수
def print_all_elements(arr):
    for element in arr:
        print(element)

# 시간 복잡도: O(n)

#########################################################

# O(n log n) - 로그 선형 시간 복잡도
# 많은 정렬 알고리즘이 이 시간 복잡도를 가집니다.

# 예시: 병합 정렬
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 시간 복잡도: O(n log n)

#########################################################

# O(n^2) - 이차 시간 복잡도
# 입력 크기가 커질수록 실행 시간이 제곱 형태로 증가하는 알고리즘입니다.
# 버블 정렬이 대표적입니다.

# 예시: 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 시간 복잡도: O(n^2)

#########################################################

# O(2^n) - 지수 시간 복잡도
# 입력 크기가 커질수록 실행 시간이 지수 형태로 증가하는 알고리즘입니다.
# 피보나치 수열을 재귀적으로 계산하는 알고리즘이 대표적입니다.

# 예시: 피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 시간 복잡도: O(2^n)

#########################################################

# O(n!) - 팩토리얼 시간 복잡도
# 가장 비효율적인 시간 복잡도로, 순열 생성 알고리즘이 이 시간 복잡도를 가집니다.

# 예시: 순열 생성
from itertools import permutations

def generate_permutations(arr):
    return list(permutations(arr))

# 시간 복잡도: O(n!)

#########################################################

# - **O(1)**: 상수 시간 복잡도 (예: 배열의 첫 번째 원소 접근)
# - **O(log n)**: 로그 시간 복잡도 (예: 이진 탐색)
# - **O(n)**: 선형 시간 복잡도 (예: 배열의 모든 원소 출력)
# - **O(n log n)**: 로그 선형 시간 복잡도 (예: 병합 정렬)
# - **O(n^2)**: 이차 시간 복잡도 (예: 버블 정렬)
# - **O(2^n)**: 지수 시간 복잡도 (예: 재귀적 피보나치 수열 계산)
# - **O(n!)**: 팩토리얼 시간 복잡도 (예: 순열 생성)

#########################################################