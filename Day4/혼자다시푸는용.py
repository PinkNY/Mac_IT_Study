# from math import ceil

# def solution(progresses, speeds):
#     answer = [0]
    
#     for progresses, speed in zip(progresses, speeds):
#         spend = ceil((100 - progresses) / speed)
#         answer.append(max(answer[-1], spend))
        
#     answer = answer[1:]
    
#     count = 0
#     temp = 0
#     result = []
    
#     for a in answer:
#         if temp != a:
#             result.append(count)
#             temp = a
#             count = 0
#         count += 1
#     result.append(count)
    
#     return result[1:]

# class Solution:
#     def dailyTemperatures(self, T: list[int]) -> list[int]:
        
#         counter = {k:0 for k in range(len(T))}
#         # 동일한 온도가 있을 수 있으므로 인덱스로.
        
#         stack = [0]
        
#         for i in range(1,len(T)):
#             temp = T[i]
#             while True:
#                 cur_idx = stack.pop()
#                 cur_temp = T[cur_idx]
                
#                 if cur_temp >= temp:
#                     stack.append(cur_idx)
#                     stack.append(i)
#                     break
#                 else:
#                     counter[cur_idx] = i-cur_idx 
#                     if not stack:
#                         stack.append(i)
#                         break
                    
#         while stack:
#             counter[stack.pop()] = 0
            
#         return list(counter.values())

# import heapq

# def solution(scoville, K):
    
#     n = 0
    
#     heapq.heapify(scoville)
    
#     while True:
#         if len(scoville) == 1 and scoville[0] < K:
#             return -1
        
#         mini = heapq.heappop(scoville)
        
#         if mini >= K:
#             return n
        
#         second = heapq.heappop(scoville)
        
#         heapq.heappush(scoville, mini + second * 2)
        
#         n += 1
        



