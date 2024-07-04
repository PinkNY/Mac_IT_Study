numbers = [23,4, 612, 354, 4]

# 정렬
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# numbers = numbers.sort() -> None

# 리스트 컴프리헨션 예제
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 코드가 간결해지므로 익숙해지면 좋다.

# 빈 딕셔너리 생성
empty_dict = {}

# 키-값 쌍을 포함한 딕셔너리 생성
person = {
    "name": "John",
    "age": 30,
    "City": "New York"
}

for key, value in person.items():
    print(key, value)
    

str1 = "Hello, World!"
str1[0] = "h"   # TypeError # 문자열은 불변.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for a,b in zip(list1, list2):
    print(a,b)

import heapq

# 빈 힙 생성
min_heap = []

# 삽입 연산
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 2)

# 힙에서 최솟값 제거 및 반환
min_value = heapq.heappop(min_heap)
print(min_value)  # 출력: 1

# 힙에서 최솟값 확인 (제거하지 않음)
min_value = min_heap[0]
print(min_value)  # 출력: 2

