# 튜플, 콜백 함수, 람다, with 구문


#%%
# 튜플

a = (1,2,3)
print("튜플의 전체", a)
print("튜플의 첫 번째 원소", a[0])

#%% 리스트

a = [1,2,3]
print("리스트의 전체", a)
print("리스트의 첫 번째 원소", a[0])

#%% 튜플과 리스트의 차이

tuple_a = (1,2,3)
list_a = [1,2,3]

# 리스트는 변경이 가능한 반면, 튜플은 변경이 불가.
# 특정한 원소를 추가, 제거, 변경 등을 하는 행위.

# 리스트에서 첫 번째 원소를 변경하고 싶다.
list_a[0] = 4
list_a.append(5)    # 리스트에 5 라는 원소를 추가
print(list_a)
#%%

tuple_a = (1,2,3)
tuple_a[0] = 4
print(tuple_a)
# %%

tuple_a = (1,2,3)
tuple_a.append(5)
print(tuple_a)

# 리스트는 변경이 가능한 자료를 다룰 때 사용
# 고객 목록 등

# 튜플은 변경이 불가능한 자료를 다룰 때 사용
# 고객 목록(고정), 설정값(고정)

#%% 튜플의 교환

a, b = 100, 200
# temp = a
# a = b
# b = temp

a, b = b, a
print(a,b)

# %% 튜플과 함수

def return_all(a,b,c):
    return a, b, c

print(return_all(10,20,30))
print(type(return_all(10,20,30)))

# %%

def return_all(*values):
    print(f'vales의 타입은 {type(values)}')
    return values

print(return_all(10,20,30))
print(type(return_all(10,20,30)))

# %% 콜백 함수와 람다

# 콜백 함수 : 함수의 매개변수에 사용하는 함수

# 매개변수로 받은 함수를 10번 호출
def call_10_times(func):
    for i in range(10):
        func()
        
# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")
    
# 조합하기    
call_10_times(print_hello)


# %% 고차 함수


#%% 반복문

# list_input_a[0] = list_input_a[0] * list_input_a[1]
# list_input_a[1] = list_input_a[1] * list_input_a[2]
# ...
# list_input_a[4] = list_input_a[4] * list_input_a[4]

# for 문 enumerate 키워드

list_input_a = [1,2,3,4,5]

def power(item):
    return item * item

for i, value in enumerate(list_input_a):
    print(i, value)
    list_input_a[i] = power(value)
    
print(list_input_a)

#%%
list_input_a = [1,2,3,4,5]

new_list_input_a = []
for number in list_input_a:
    new_list_input_a.append(number * number)
print(new_list_input_a)

#%%

# map(함수, 리스트)

def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)

print(list(output_b))

#%%

# 리스트 컨프리헨션
print([x * x for x in list_input_a])
print([x * x for x in list_input_a if x < 300])

#%%
# lambda 함수

output_b = filter(lambda x: x < 300, list_input_a)
print(list(output_b))

output_a = map(lambda item: item * item, list_input_a)

#%%
# with 함수 : 파일 작업

# open 함수(파일 열기)

with open('Day2/basic.txt', 'r') as file:
    contents = file.read()
    
print(contents)
# %%
