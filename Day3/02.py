numbers = [10, 20, 30, 40, 50]

# 원소의 첫 번째 접근. 0번 째 인덱스 접근
print(numbers[0])

# 원소의 마지막에 접근.
print(numbers[-1])

# 원소의 항목 변경
numbers[0] = 100
print(numbers)

# 항목 추가
numbers.append(60)
print(numbers)

# 항목 삽입
numbers.insert(2, 25)
print(numbers)

# 항목 제거
numbers.remove(30)
print(numbers)

if 30 in numbers:
    numbers.remove(30)
    
try:
    numbers.remove(30)
except:
    pass
print(numbers)

# Pop (항목 맨 뒤 값 제거)
last_item = numbers.pop()
print(last_item)
print(numbers) 

# 항목 포함 여부 확인
print(20 in numbers)
print(70 in numbers)

# extend() 리스트에 항목 추가.
numbers.extend([70, 80])
print(numbers)

# sort() 기본 오름차순, 매개변수 reverse=True 내림차순
numbers.sort(reverse=True)
print(numbers)

# resverse() 리스트의 항목 순서를 반대로 뒤집는다.
numbers.reverse()
print(numbers)

# 슬라이싱
numbers = numbers[::-1]
print(numbers[:5])  # numbers[0:5:1]
print(numbers[2:5]) # numbers[2:5:1]
print(numbers[:-5])  # numbers[0:-5:1]
print(numbers[5:])  # numbers[5:len(n)-1:1]
print(numbers[::2]) # 2 간격으로 
print(numbers[::-2]) # 2 간격으로 역순

# index() 특정 항목의 첫 번째 인덱스를 반환.
index = numbers.index(50)
print(index)

# count() 리스트 내에서 특정 항목이 몇 번 등장하는지.
count = numbers.count(25)
print(count)

#######################################################

def solution(num_list):
    for index, num in enumerate(num_list):
        if num < 0:
            return index
    else:
        return -1
    
#######################################################

