graph = {
    1: [2, 3, 4],   # 부모 노드
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def recursive_dfs(v, discovered=[]):
    
    print(f'recrusive_dfs 진입 : 탐색하는 정점: {v}, 여태까지 경로: {discovered=}')
    print()
    
    discovered.append(v)

    
    print(f'append 함수 호출 : 여태까지 경로 {discovered}')
    print()
    
    print(f'for문 진입 : 탐색한 정점 {v}와 연결된 노드들은 {graph[v]}이고 연결된 노드들을 하나씩 탐색합니다.')
    print()
    
    for w in graph[v]:
        if w not in discovered:
            print(f'if문 진입 : 정점 {w}는 아직 탐색하지 않았기 때문에 재귀함수를 호출합니다.')
            print()
            
            discovered = recursive_dfs(w, discovered)
            
            print(f'재귀함수 종료 : 정점 {w}에 대한 재귀함수가 종료되었습니다.')
            print()
            
    return discovered

print(f'{recursive_dfs(1)=}')

# 1. recursive_dfs 함수를 정의.
# 2. discovered에 v를 추가한다.
# 3. w가 graph[v] 안에 있을때.
# 4. 만약 w가 discovered 안에 없다면.
# 5. discovered에 recursive_dfs를 넣는다.
# 6. 반복.
# 7. discovered를 반환한다.
# 8. f string 이용하여 값을 출력.

# recrusive_dfs 진입 : 탐색하는 정점: 1, 여태까지 경로: discovered=[]

# append 함수 호출 : 여태까지 경로 [1]

# for문 진입 : 탐색한 정점 1와 연결된 노드들은 [2, 3, 4]이고 연결된 노드들을 하나씩 탐색합니다.

# if문 진입 : 정점 2는 아직 탐색하지 않았기 때문에 재귀함수를 호출합니다.

# recrusive_dfs 진입 : 탐색하는 정점: 2, 여태까지 경로: discovered=[1]

# append 함수 호출 : 여태까지 경로 [1, 2]

# for문 진입 : 탐색한 정점 2와 연결된 노드들은 [5]이고 연결된 노드들을 하나씩 탐색합니다.

# if문 진입 : 정점 5는 아직 탐색하지 않았기 때문에 재귀함수를 호출합니다.

# recrusive_dfs 진입 : 탐색하는 정점: 5, 여태까지 경로: discovered=[1, 2]

# append 함수 호출 : 여태까지 경로 [1, 2, 5]

# for문 진입 : 탐색한 정점 5와 연결된 노드들은 [6, 7]이고 연결된 노드들을 하나씩 탐색합니다.

# if문 진입 : 정점 6는 아직 탐색하지 않았기 때문에 재귀함수를 호출합니다.

# recrusive_dfs 진입 : 탐색하는 정점: 6, 여태까지 경로: discovered=[1, 2, 5]
# ...

# 재귀함수 종료 : 정점 4에 대한 재귀함수가 종료되었습니다.


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        print(f'while문 진입 - 앞으로 탐색할 노드들 : {stack=} ')
        v = stack.pop()
        print(f'stack에서 값을 하나 뺌 : {v=} : ')
        if v not in discovered:
            discovered.append(v)
            print(f'아직 탐색에 추가되지 않은 v 추가 : {discovered=} : ')
            for w in graph[v]:
                stack.append(w)
                print(f'정점 {v=}와 연결된 노드들을 {stack=}에 추가  : {v=} : ')
    return discovered

print(f'{iterative_dfs(1)=}')

# iterative_dfs(1)=[1, 4, 3, 5, 7, 6, 2]

def iterative_dfs(start_v):
    # start_v는 탐색을 시작할 노드. iterative_dfs 함수 설정.
    discovered = []
    # 빈 discovered 를 하나 생성 해둔다.
    stack = [start_v]
    # stack에 탐색을 시작할 노드(start_v)를 추가한다.
    while stack:
        v = stack.pop()
    # stack이 비어 있지 않는 동안 반복문을 계속 실행한다.
    # 탐색이 시작되면 stack에 계속 추가가 되며 마지막에 추가된게 계속 실행된다.
    # stack에서 노드를 하나 꺼내어 v에 추가한다.
        if v not in discovered:
            discovered.append(v)
    # v가 discovered 리스트에 없다면, v를 discovered 리스트에 추가한다.
            for w in graph[v]:
                stack.append(w)
    # v와 연결된 노드 w 들을 스택에 추가한다.
    # if문에서 v가 discovered리스트에 유무를 확인하고 리스트에 추가하는 과정을 하기 위해.
    # 다음에 탐색할 노드들을 스택에 저장해주는 역활.
    return discovered
    # 탐색을 완료하고 결과값을 반환한다.
print(f'{iterative_dfs(1)=}')
    # 함수를 호출하여 탐색을 시작한다.

# while문 진입 - 앞으로 탐색할 노드들 : stack=[1] 

# stack에서 값을 하나 뺌 : v=1 : 

# 아직 탐색에 추가되지 않은 v 추가 : discovered=[1] : 

# 정점 v=1와 연결된 노드들을 stack=[2]에 추가  : v=1 : 

# 정점 v=1와 연결된 노드들을 stack=[2, 3]에 추가  : v=1 : 

# 정점 v=1와 연결된 노드들을 stack=[2, 3, 4]에 추가  : v=1 : 

# while문 진입 - 앞으로 탐색할 노드들 : stack=[2, 3, 4] 

# stack에서 값을 하나 뺌 : v=4 : 

# 아직 탐색에 추가되지 않은 v 추가 : discovered=[1, 4] : 

# while문 진입 - 앞으로 탐색할 노드들 : stack=[2, 3] 

# stack에서 값을 하나 뺌 : v=3 : 

# 아직 탐색에 추가되지 않은 v 추가 : discovered=[1, 4, 3] : 

# 정점 v=3와 연결된 노드들을 stack=[2, 5]에 추가  : v=3 : 
# ...

# stack에서 값을 하나 뺌 : v=5 : 

# iterative_dfs(1)=[1, 4, 3, 5, 7, 6, 2]

# start_v는 탐색을 시작할 노드. iterative_dfs 함수를 정의하고 비어있는 discovered를 생성해둔다.
# stack에는 start_v를 추가하여 stack에서 노드를 하나씩 탐색 할 수 있게 해준다.
# 그 후 while문을 통하여 stack이 비어 있지 않는 한 계속 반복문을 진행한다.
# 반복문 내용은 v가 discovered 리스트 안에 없다면 v를 discovered 리스트에 추가하겠다. 라는 반복을 한다.
# 그리고 그 반복을 진행하게 하기 위해 v와 연결되어 있는 w들을 스택에 추가해준다.
# 아직 탐색하지 않는 노드들은 계속 stack에 추가하고 그 stack이 비어질때 까지 진행한다.
# 그 후 탐색이 끝나면 return discovered를 하여 결과값을 반환하고 print문으로 출력해서 탐색을 시작한다.


def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    # 탐색된 노드를 저장할 리스트와 탐색할 노드를 저장할 큐를 초기화합니다.
    
    print(f'초기 상태: discovered={discovered}, queue={queue}')
    
    while queue:
        v = queue.pop(0)
    # 큐가 비어 있지 않은 동안 탐색을 계속합니다.
        print(f'노드 {v} 탐색 중, queue={queue}')
        
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
        # 현재 노드 v와 연결된 모든 노드들을 순회합니다.
        # w가 discovered 리스트에 없다면 w를 discovered 리스트와 queue에 추가한다.
                print(f'노드 {v}와 연결된 노드 {w}를 발견: discovered={discovered}, queue={queue}')
                
    return discovered

print(f'{iterative_bfs(1)=}')

    
# iterative_bfs(1)=[1, 2, 3, 4, 5, 6, 7]

# from collections import deque

# def iterative_bfs(start_v):
#     discovered = [start_v]
#     queue = [start_v]
# # iterative_bfs를 정의. discovered와 queue 를 생성 하여 각각 start_v를 넣어둔다.
# # discovered에는 탐색된 노드를 저장. queue에는 탐색 할 노드를 저장한다.
# # 처음엔 start_v를 넣어서 초기화 시킴.

#     while queue:
#         v = queue.pop(0)
    
#         for w in graph[v]:
#             if w not in discovered:
#                 discovered.append(w)
#                 queue.append(w)
                
#     # 큐가 비어 있지 않는 한 계속 탐색한다.
#     # 현재 노드 v와 연결된 모든 노드들(w)를 순회하고
#     # 탐색 한 노드를 discovered에 추가한다.
#     # 남은 탐색 할 노드는 queue에 추가한다.
    
#     return discovered
#     # 모든 탐색이 끝나면 discovered를 반환한다.

# print(f'{iterative_bfs(1)=}')


# leetcode 200 문제

# class Solution:
#     from collections import deque
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         d=[(0,1),(0,-1),(1,0),(-1,0)] 
        
#         answer=0
#         visited=[[False]*n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]=="1":
                    
#                     # bfs
#                     q=deque([(i,j)])
#                     while q:
#                         x,y=q.popleft()
#                         for dx,dy in d:
#                             nx,ny=x+dx,y+dy
#                             if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
#                                 grid[nx][ny]="0"
#                                 q.append((nx,ny))
#                     answer+=1
                    
#         return answer


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(x,y):
#             if x in range(len(grid)) and \
#                 y in range(len(grid[0])) and \
#                 grid[x][y] == '1':
#                     grid[x][y] = '0'
#                     dfs(x + 1, y)
#                     dfs(x, y + 1)
#                     dfs(x - 1, y)
#                     dfs(x, y - 1)
        
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     dfs(i,j)
#                     count += 1
                    
#         return count



# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def dfs(index, path):
#             # 끝까지탐색하면 백트래킹
            
#             if len(path) == len(digits):
#                 result.append(path)
#                 return
            
#             # 입력값 자릿수 단위 반복
#             for i in range(index, len(digits)):
#                 for j in dic[digits[i]]:
#                     dfs(i + 1, path + j)
#         # 예외 처리         
#         if not digits:
#             return []
        
#         dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#                "6": "mno","7": "pqrs", "8": "tuv", "9": "wxyz"}
#         result = []
#         dfs(0, "")
        
#         return result


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if digits == "":
#             return []
#         def dfs(index, path):   # dfs(1, 'a')
            
#             if len(path) == len(digits):
#                 result.append(path)
#                 return
            
#             for i in range(index, len(digits)):
#                 # digiits의 길이만큼, digits=23 -> 2번
#                 for j in num_to_alpha[digits[i]]:
#                     # j 가 항상 3번 digiths=23, a,bc
#                     dfs(i + 1, path + j)
                
#         num_to_alpha = {
#             "2": "abc", "3": "def", "4": "ghi",
#             "5": "jkl", "6": "mno", "7": "pqrs",
#             "8": "tuv", "9": "wxyz"
#             }

#         result = []
#         dfs(0, "")
#         return result


# class Solution2:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#     	# remainder 개념을 사용한 이유는 빈 리스트가 입력으로 들어왔을 때도 동일하게 동작하기 위함
#         def dfs(level: int, partial_list: List, remainder: int):
#             if len(partial_list) == k:
#                 answer.append(partial_list)
#                 return
#             for i in range(remainder, n-k+level+1):
#                 dfs(level+1, partial_list + [i], i+1)

#         answer = []
#         dfs(1, [], 1)
#         return answer

