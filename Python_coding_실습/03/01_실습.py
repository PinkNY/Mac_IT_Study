import time

def is_even(n):
    return n % 2 == 0

# n = 1000000
# start = time.time()
# is_even(n)
# end = time.time()
# print(f"Execution time: {end - start} seconds")

numbers = list(range(10000))

start = time.time()
for n in numbers:
    if n % 1000 == 0:
        print(n)
end = time.time()
print(f"Execution time: {end - start} seconds")

#########################################################

import time

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = list(range(1000000))
start = time.time()
sum_array(arr)
end = time.time()
print(f"Execution time: {end - start} seconds")

#########################################################

import time

def contains_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

arr = list(range(1000000)) + [0]
start = time.time()
contains_duplicate(arr)
end = time.time()
print(f"Execution time: {end - start} seconds")

#########################################################

import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = list(range(1000, 0, -1))
start = time.time()
selection_sort(arr)
end = time.time()
print(f"Execution time: {end - start} seconds")

#########################################################

import time

def find_sum_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = list(range(1000))
target = 1998
start = time.time()
find_sum_pairs(arr, target)
end = time.time()
print(f"Execution time: {end - start} seconds")

#########################################################

def find_sum_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
                
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
                
    return pairs
