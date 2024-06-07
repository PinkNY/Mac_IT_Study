# 복습 문제 3번

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#     except TypeError:
#         return "올바른 타입이 아닙니다."
        

# result = divide(10, 2)
# print(result)  # 출력: 5.0

# result = divide(10, 0)
# print(result)  # 출력: Cannot divide by zero

# result = divide(10, '0')
# print(result)  # 출력: 올바른 타입이 아닙니다.

# 복습 문제 6번

# import random

# def generate_lotto_numbers():
#     generated = set()
#     while len(generated) < 6:
#         random_number = random.randint(1,45)
#         generated.add(random_number)
#     return generated

# print(generate_lotto_numbers())
# 집합 사용
        
# set(집합)은 add 를 이용하여 추가.
# a = set()
# a.add(100)
# a.add(100)
# a.add(100)
# a.add(100)
# print(a)

# import random

# def generate_lotto_numbers():
#     generated = []
#     while len(generated) < 6:
#         random_number = random.randint(1,45)
#         if random_number not in generated:
#             generated.append(random_number)
#     return generated

# print(generate_lotto_numbers())
# 리스트 사용.
# 랜덤값이라 미리 변수에 저장 해두고 사용.
# 그때 그때 넣어서 쓰면 랜덤값이라 조건문 돌때 값이 달라짐

# 복습 문제 7번

# class Book:
#     def __init__(self, title, author, year):
#         # 여기에 코드를 작성하세요
#         self.title = title
#         self.author = author
#         self.year = year
#         # 객채 생성

#     def description(self):
#         # 여기에 코드를 작성하세요
#         return f"{self.title} by {self.author}, published in {self.year}"

#     def is_classic(self):
#         # 여기에 코드를 작성하세요
#         # if 2024 - self.year >= 70:
#         #     return True
#         # else:
#         #     return False
#         return 2024 - self.year >= 70

# # 객체 생성 및 사용 예시
# book1 = Book("1984", "George Orwell", 1949)
# book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# print(book1.description())  # 출력: 1984 by George Orwell, published in 1949
# print(book2.description())  # 출력: The Great Gatsby by F. Scott Fitzgerald, published in 1925
# print(book3.description())  # 출력: To Kill a Mockingbird by Harper Lee, published in 1960

# print(book1.is_classic())  # 출력: True
# print(book2.is_classic())  # 출력: True
# print(book3.is_classic())  # 출력: False

# 복습 문제 12번

# def list_methods(my_list):
#     # 1. 3을 리스트의 맨 끝에 추가하세요
#     my_list.append(3)
#     # my_list = my_list + [3]
#     # 2. 5를 리스트의 첫 번째 위치에 추가하세요
#     my_list.insert(0,5)
#     # 3. 리스트의 첫 번째 요소를 제거하세요
#     my_list.pop(0)
#     # 4. 리스트를 오름차순으로 정렬하세요
#     my_list.sort()

# example_list = [4, 2, 1, 5]
# list_methods(example_list)
# print(example_list)  # 출력: [1, 2, 3, 4, 5]

# a = [1,2,3]   # address copy
# b = a         # value copy
# c = a.copy()
# a[0] = 4
# print(b,c)
# 참조값, 값.

# 복습 문제 14번

# def check_duplicate_keys(dict1, dict2):
#     # 여기에 코드를 작성하세요
#     duplicated = set()
    
#     for key1 in dict1.keys():
#         if key1 in dict2.keys():
#             duplicated.add(key1)
            
#     for d in duplicated:
#         print(f"Key {d} is duplicated")

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# check_duplicate_keys(dict1, dict2)
# # 출력:
# # Key b is duplicated

# 복습 문제 18번

# def set_operations(set1, set2):
#     # 여기에 코드를 작성하세요
#     union_set = set1.union(set2)
#     # union_set = set1 | set2
#     intersection_set = set1.intersection(set2)
#     # set1 & set2
#     difference_set = set1.difference(set2)
#     # set1 - set2
#     return union_set, intersection_set, difference_set

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result = set_operations(set1, set2)
# print(result)  # 출력: ({1, 2, 3, 4}, {2, 3}, {1})


# 1~7번에 해당하는 Key가 정점

# number = 100
# # 출력 결과 : number=100
# print(f'number={number}')
# print(f'{number=}') # 파이썬 최신버전에선 가능한 문법.


# graph = {
#     1: [2, 3, 4],   # 부모 노드
#     2: [5],
#     3: [5],
#     4: [],
#     5: [6, 7],
#     6: [],
#     7: [3],
# }

# def recursive_dfs(v, discovered=[]):
#     print(f'recrusive_dfs 진입 : 탐색하는 정점: {v}, 여태까지 경로: {discovered=}')
#     # 우리가 탐색한 경로
#     discovered.append(v)
#     print(f'append 함수 호출 : 여태까지 경로 {discovered}')
#     #print(f'for문 진입 : 탐색한 정점 {v}를 여태까지 경로에 추가합니다.')
#     print(f'for문 진입 : 탐색한 정점 {v}와 연결된 노드들은 {graph[v]}이고 연결된 노드들을 하나씩 탐색합니다.')
#     for w in graph[v]: # 정점과 연결된 다른 정점
#         if w not in discovered: # 이미 탐색한 정점은 거르기
#             print(f'if문 진입 : 정점 {w}는 아직 탐색하지 않았기 때문에 재귀함수를 호출합니다.')
#             discovered = recursive_dfs(w, discovered)
#             print(f'재귀함수 종료 : 정점 {w}에 대한 재귀함수가 종료되었습니다.')
#     return discovered
    
# print(f'{recursive_dfs(1)=}')











