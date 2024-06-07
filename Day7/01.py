# 탐색 알고리즘 복습
# 리트코드 46번 문제

# dfs
# discovered : 탐색 경로 (결과)
# 재귀 호출 or 스택(stack) 탐색할 노드들

# dfs([1,2,3])      - 부모
# dfs([1,2]),[3]    - 1차
# dfs([1]),[3,2]    - 2차
# dfs([]), [3,2,1] -> result = [[3,2,1]] - 3차
# dfs([2]), [3,1] -> 2차
# dfs([]), [3,1,2] - 3차
# dfs([1,3]), [2] -> 1차

# from typing import List
# class Solution:
    
#     def permute(self, nums): # List[int]) -> List[List[int]]:
#         result = []
#         prev_elements = []
        
#         def dfs(elements):
    
#             print(f'dfs 진입: 여태까지 조합 {prev_elements=}, 남은 조합 {elements=}')
            
#             if len(elements) == 0:
#                 result.append(prev_elements[:]) # 값 복사 추가
            
#             # dfs([1,2,3]) -> dfs([1,2]) [3] 새로운 함수
#             for e in elements:
#                 # elements 값을 복사
#                 next_elements = elements[:]
#                 # remove 연산 0(n)
#                 next_elements.remove(e)
#                 # next_elements = [1,2]
                               
#                 prev_elements.append(e)
#                 dfs(next_elements)
#                 prev_elements.pop()

#         dfs(nums)    
#         return result

# Solution = Solution() # instance(object) = constructor
# Solution.permute([1,2,3])   # method

# from typing import List

# class Solution:
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         prev_elements = []
        
#         def dfs(elements):
#             print(f'dfs 진입: 여태까지 조합 {prev_elements=}, 남은 조합 {elements=}')
            
#             if len(elements) == 0:
#                 result.append(prev_elements[:])
#                 print(f'조합 완성: {prev_elements[:]}, result에 추가됨')
#                 return
            
            # for e in elements:
            #     next_elements = elements[:]
            #     next_elements.remove(e)
                
            #     prev_elements.append(e)
            #     print(f'원소 추가: {e}, {prev_elements=}, {next_elements=}')
            #     dfs(next_elements)
            #     prev_elements.pop()
            #     print(f'원소 제거: {e}, {prev_elements=}, {next_elements=}')
        
#         dfs(nums)
#         return result

# # 예시 실행
# solution = Solution()
# permutations = solution.permute([1, 2, 3])
# print(f'최종 결과: {permutations}')

# class Solution:
#     def permute(self, nums):
#         stack = [([], nums)]
#         result = []
        
#         while stack:
#             perm, items = stack.pop()
#             if len(items) == 0:
#                 result.append(perm)
                
#             for i in range(len(items)):
#                 new_perm = perm + [items[i]]
#                 new_items = items[:i] + items[i + 1:]
#                 stack.append((new_perm, new_items))
#                 print(new_perm, new_items)
                
#         return result


# class Solution:
#     def permute(self, nums):
#         stack = [([], nums)]
#         result = []
        
#         while stack:
#             prev_elements, elements = stack.pop()
#             print(f'스택 팝: 현재 prev_elements {prev_elements=}, 남은 elements {elements=}\n')
            
#             if len(elements) == 0:
#                 result.append(prev_elements[:])
#                 print(f'순열 완성: {prev_elements[:]}, result에 추가됨\n')
                
#             for e in elements:
#                 next_elements = elements[:]
#                 next_elements.remove(e)
#                 stack.append((prev_elements + [e], next_elements))
#                 print(f'스택 푸시: 업데이트된 prev_elements {prev_elements + [e]=}, 새로운 elements {next_elements=}\n')
                
#         return result

# # 예시 실행
# solution = Solution()
# permutations = solution.permute([1, 2, 3])
# print(f'최종 결과: {permutations}')

# from types import List
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         output = []
#         nums = [ i + 1 for i in range(n)]
        
#         def dfs(k, stack=None):
#             if stack is None:
#                 stack = []
                
#             if k == 0:
#                 output.append(stack)
#                 return
            
#             if stack:
#                 for w in nums[stack[-1]-1:]:
#                     if w not in stack:
#                         dfs(k-1, stack + [w])
                        
#             else:
#                 for w in nums:
#                     if w not in stack:
#                         dfs(k-1, stack + [w])
                        
#         dfs(k)
        
#         return output
        
# class Solution:
#     def combine(self, n, k):
#     # k는 조합의 길이. n은 시작부터 끝까지의 숫자 범위.
#         result = []
#         stack = [(1, [])]
#         # 빈 result 리스트와 stack(스택)을 초기화.
#         # 스택에는 튜플 형태(start, elements)로 들어간다.
#         # start는 시작 인덱스. elements는 현재까지의 조합.
#         # 초기 상태에서는 시작 인덱스는 1이고, 현재까지 조합은 빈 리스트.
        
#         while stack:
#             start, elements = stack.pop()
#             print(f'스택 팝: 현재 start={start}, 현재 elements={elements}')
#             # 스택이 빌 때까지 반복.
#             # 스택에서 요소를 팝하여 start(시작 인덱스)와 elements(현재까지의 조합)으로 분리.
            
#             if len(elements) == k:
#                 result.append(elements[:])
#                 print(f'조합 완성: {elements}, result에 추가됨')
#                 continue # 밑에 코드로 넘어가지 않고 바로 다음 반복을 실행.
#             # elements의 길이가 k와 같으면 현재 조합이 완성 이므로 결과 리스트에 추가.
#             # 이후 다음 반복으로 넘어감.
            
#             for i in range(start, n + 1):
#                 stack.append((i + 1, elements + [i]))
#                 print(f'스택 푸시: 다음 start={i + 1}, 다음 elements={elements + [i]}')
#             # start부터 n까지 순회 하면서 스택에 다음 요소를 추가.
#             # start는 현재까지의 조합에서 가장 큰 숫자보다 1 큰 값을 가진다.
#             # 새로운 요소를 추가한 조합은 새로운 시작 인덱스와 함께 스택에 추가.
                
#         return result
#         # 완성된 모든 조합들을 담은 결과 리스트를 반환.

# # 예시 실행
# solution = Solution()
# combinations = solution.combine(4, 2)
# print(f'조합 결과: {combinations}')

# def bubble_sort(arr):
#     n = len(arr)
#     # 배열의 길이를 n에 추가.
    
#     # 이중 반복문
#     for i in range(n):
#     # 배열의 길이(n) 만큼 반복.
#     # 각 반복에서 정렬 범위의 끝 부분(마지막 원소)를 제외하고 정렬 수행.
#     # 각 반복마다 가장 큰 원소가 배열의 마지막으로 이동.
#         for j in range(0, n - i - 1):
#         # 현재 정렬 범위 내에서 인접한 원소를 비교하고 필요하다면 위치를 바꾼다.
#         # j 는 현재 원소의 인덱스. 0 부터 시작하여 정렬 범위 끝까지 이동.
#         # n -i -1 = 현재 정렬 범위 내에서 비교할 수 있는 마지막 인덱스.
#         # 외부 반복문이 실행될 때마다 정렬 범위가 감소하기에 -i를 추가하여 정렬 범위를 줄임.
#             if arr[j] > arr[j + 1]:
#             # arr[j] (현재 원소) 와 arr[j + 1] (다음 원소)를 비교.
#             # 현재 원소가 다음 원소보다 크다면 위치를 교환.
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 # 현재 정렬 범위 내에서 가장 큰 원소가 오른쪽으로 이동하여 정렬.
#     return arr

# # 테스트
# data = [64, 34, 25, 12, 22, 11, 90]
# print("Bubble Sort 결과:", bubble_sort(data))

# def bubble_sort(arr):
#     n = len(arr)
    
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# data = [64, 34, 25, 12, 22, 11, 90]
# print("Bubble Sort 결과:", bubble_sort(data))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#     #정렬할 값 지정
#         print(f'현재 인덱스 i: {i}, 정렬 전 배열: {arr}')
#         # range(1,7) -> 1, 2, 3, 4, 5, 6
#         key = arr[i]
#         # 정렬할 값의 왼쪽 인덱스 가져오기
#         print(f'현재 key 값: {key}')
#         # arr[1], .... arr[6]
#         j = i - 1
#         # 0, 1, 2, 3, 4, 5
#         while j >= 0 and key < arr[j]:
#             print(f'{i=}정렬 전 : {arr=}, {j+1=}, {j=}')
#             arr[j + 1] = arr[j]
#             print(f'{i=}정렬 후 : {arr=}, {j+1=}, {j=}')
#             j -= 1
#         arr[j + 1] = key
#         # j 인덱스를 가장 왼쪽까지 이동시킨 후 값 복구
#         print(f'한 번의 정렬이 끝난 후 배열 상태: {arr}')
#         # 앞에 있는 값이 뒤에 있는 값보다 클때까지
#         # 정렬이 안되어 있다면, j가 음수이면 list out of range 에러 발생.
#     return arr

# # 테스트
# data = [64, 34, 25, 12, 22, 11, 90]
# print("Insertion Sort 결과:", insertion_sort(data))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i
        
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
        
#     return arr

# data = [64, 34, 25, 12, 22, 11, 90]
# print("Insertion Sort 결과:", insertion_sort(data))

# data = [64, 34, 25, 12, 22, 11, 90]

# # 기본 정렬 (오름차순)
# sorted_data = sorted(data)
# print("오름차순 정렬:", sorted_data)

# # 기본 정렬 (내림차순)
# sorted_data = sorted(data, reverse=True)
# print("내림차순 정렬:", sorted_data)

# # 키를 사용한 정렬 (길이를 기준으로 정렬)
# words = ["apple", "banana", "cherry", "date"]
# sorted_words = sorted(words, key=len)
# print("길이 기준 정렬:", sorted_words)

# import sys
# input = sys.stdin.readlines

# n = int(input())

# arr = []
# for _ in range(n):
#     arr.append(int(input()))
    
# arr = sorted(arr)
# # arr.sort()
# print(arr)

# x = []

# for i in range(5):
#     x.append(int(input()))
# x.sort()

# print(int(sum(x)/5))
# print(x[2])

# n, m = map(int,input().split())

# scores = list(map(int,input().split()))
# scores.sort(reverse=True)

# print(scores[m-1])

# n = int(input())

# m = []

# for i in str(n):
#     m.append(int(i))
# # m = list(map(int,str(n))) 으로 변경 가능.
    
# m.sort(reverse=True)

# for i in m:
#     print(i,end='')

# arr = sorted(input(), reverse=True)

# for element in arr:
#     print(element, end='')

# arr = ''.join(sorted(input(), reverse=True))
# print(arr)

# n = int(input())
# arr = []

# for i in range(n):
#     a,b = map(int,input().split())
#     arr.append((a,b))
# arr.sort()

# for i in range(n):
#     print(arr[i][0],arr[i][1])

# n = int(input())
# # coordinates = 좌표
# coords = [list(map(input().split() for _ in range(n)))]
# coords.sort()

# for x, y in coords:
#     print(x, y)

# students = [
#     {"name": "John", "age": 25, "grade": 85},
#     {"name": "Jane", "age": 22, "grade": 90},
#     {"name": "Anna", "age": 22, "grade": 91},
#     {"name": "Dave", "age": 23, "grade": 88},
#     {"name": "Alice", "age": 24, "grade": 95}
# ]

# # 나이와 성적 기준으로 정렬 (먼저 나이, 그 다음 성적)
# sorted_by_age_then_grade = sorted(students, key=lambda x: (x["age"], x["grade"]))
# print("나이와 성적 기준 정렬:", sorted_by_age_then_grade)

# import sys
# n=int(input())
# li=[]
# for i in range(n):
#     a, b = map(int,sys.stdin.readline().split())
#     li.append([a,b])
# li.sort(key=lambda x: (x[1], x[0]))
# for i in li:
#     print(i[0], i[1])




# n = int(input())
# m = []

# for i in range(n):
#     a, b = map(int,input().split)
#     m.append([a,b])
    
# m.sort(key=lambda x: (x[1], x[0]))

# for i in m:
#     print(i[0], i[1])

# n = int(input())

# coords = [list(map(int(input().split()))) for _ in range(n)]

# sorted_coords = sorted(coords, key=lambda x: x[1])
# # sorted(coords, key=lambda x: (x[1], x[0]))

# for x, y in sorted_coords:
#     print(x, y)

# def solution(array, commands):
#     answer = []
    
#     for i in commands:
#         ary = array[i[0]-1: i[1]]    # 문제에서 주어진 크기만큼 자르기
#         ary.sort()    # sort 함수로 정렬
#         answer.append(ary[i[2]-1])    # k 번째 값 집어넣기
        
#     return answer


# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))


def solution(citations):
    citations.sort(reverse = True)
    # 논문 인용 횟수 리스트를 역정렬함.
    answer = 0
    for i in range(len(citations)):
    # 가장 인용횟수가 많은 논문부터 돌게 됨.
        if citations[i] > answer:
        # 만약 i번째로 인용횟수가 많은 논문의 횟수가 현재 h-i
            answer = i + 1
            # index는 지금까지 돈 논문의 갯수로 고친다.
            # 반복하다보면 그 이하의 논문들은 알아서 밑에 깔린다.
            # 처음에 역정렬 해놨기 때문에.
            
        else:
            break
        
    return answer
        
    


