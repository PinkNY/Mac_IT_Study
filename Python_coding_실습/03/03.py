# 빈 딕셔너리 생성
empty_dict = {}

print(type(empty_dict))

# 딕셔너리 생성
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 항목 접근
print(person["name"])
print(person["hobby"])
print(person.get("age"))

# 항목 추가 및 수정
person["email"] = "john@example.com" # 추가
person["age"] =31 # 수정

# 항목 제거
del person["city"]
print(person)

del person["hobby"] #keyError

email = person.pop("email")
print(email)
print(person)

# 모든 항목 제거
person.clear()
print(person)

# 딕셔너리의 주요 메서드
print(person.keys()) # 키
print(person.values()) #값

keys = person.keys()
print(list(keys)[0])

print(person.items()) # key-value

for key, value in person.item():
    print(key, value)
    
person.update({"age": 32, "city": "Boston"})
print(person)

# 집합
my_set = {"apple", "banana", "cherry", "cherry"}
print(my_set)
print(type(my_set))

a = list(set([1, 2, 3, 3, 3]))
print(a)

######################################################