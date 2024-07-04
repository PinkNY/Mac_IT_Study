stack = []

# push 연산 (데이터 추가)
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# pop 연산 (가장 위에 있는 원소 삭제)
# stack.pop()
top_element = stack.pop()

print(stack)

# peak 연산 (가장 위에 있는 원소 조회)
top_element = stack[-1]

print(stack, top_element)

# is_empty 연산
is_empty = len(stack) == 0

print(is_empty)

#################################

from collections import deque

queue = deque()

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
front_element = queue.popleft()

print(queue, front_element)

# peak
front_element = queue[0]

# is_empty
is_empty = len(queue) == 0

###############################

deq = deque([1,2,3,4,5])

# rotate
deq.rotate(1)
print(deq)


 #########################
 
import heapq

min_heap = []

#삽입
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 2)
 
 
min_value = heapq.heappop(min_heap)
min_value = heapq.heappop(min_heap)
min_value = heapq.heappop(min_heap)

print(min_heap)
print(min_value) 
 
 
 
 
 
 