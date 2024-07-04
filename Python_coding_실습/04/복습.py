def example1(n):
	for i in range(n):
		for j in range(n):
			print(i, j)
   
def example2(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] not in result:
            result.append(lst[i])
    return result

def example3(dct, keys):
    result = []
    for key in keys:
        if key in dct:
            result.append(dct[key])
    return result

def example4(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

# 주어진 리스트에서 중복된 요소를 제거하고, 결과를 반환하는 함수를 작성하시오.

def remove_duplicates(lst):
	return list(set(lst))

print(remove_duplicates([1, 2, 3, 2, 4, 3, 5]))

def modify_list(lst):
    # 리스트에 값 추가
    lst.append(4)
    lst.insert(2, 5)

    # 리스트에서 값 제거
    lst.remove(1)
    lst.pop(3)

    return lst

# 예시 입력
lst = [1, 2, 3, 1, 2, 3]
print(modify_list(lst))

# 예상 출력
# [2, 5, 3, 1, 3, 4]

def word_count(string):
    words = string.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(word_count("apple banana apple orange banana"))

def print_dict(dct):
    for key, value in dct.items:
        print(f"키: {key}, 값: {value}")

# 예시 입력
dct = {'사과': 2, '바나나': 3, '오렌지': 1}
print_dict(dct)

# 예상 출력
# 키: 사과, 값: 2
# 키: 바나나, 값: 3
# 키: 오렌지, 값: 1

def get_value(dct, key):
    # 딕셔너리에서 키를 사용하여 값에 접근하기
    return dct[key]

# 예시 입력
dct = {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
print(get_value(dct, 'name'))
print(get_value(dct, 'age'))

# 예상 출력
# Alice
# 25

def add_entry(dct, key, value):
    # 딕셔너리에 항목 추가하기
    pass
    
# 예시 입력
dct = {'name': 'Alice', 'age': 25}
new_key = 'city'
new_value = 'Seoul'
print(add_entry(dct, new_key, new_value))

# 예상 출력
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}

def add_entry(dct, key, value):
    # 딕셔너리에 항목 추가하기
    dct[key] = value
    return dct
    
# 예시 입력
dct = {'name': 'Alice', 'age': 25}
new_key = 'city'
new_value = 'Seoul'
print(add_entry(dct, new_key, new_value))

# 예상 출력
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}