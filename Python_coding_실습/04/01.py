# 문자열의 기본 연산

# 인덱싱
# word = "Python"
# print(word[0])
# print(word[-1])

# 슬라이싱
# [start:end:stride]
# word = "Python"
# print(word[0:len(word):1])

# 길이 확인
# print(len(word))

# 문자열 결합 * 병합
# greeting = "Hello, " + "World!"
# print(greeting)

# 문자열 분할
text = "apple,banana,cherry"
fruits = text.split(",")
# print(fruits)

# 반복문
# for i, fruit in enumerate(fruits):
#     fruits[i] = fruit.strip

# print(fruits)

# 고차함수
# fruits = list(map(lambda x: x.strip(), fruits))

# print(fruits)

# 리스트 컨프리헨션
# fruits = [fruit.strip() for fruit in fruits]
# print(fruits)

# 문자열 결합
text = "_".join(fruits)
print(text)

# 문자열 검색 및 대체
text = "Hello, World!"
print(text.find("World!"))
print(text.replace("World!", "Python"))


# 접두사 확인하기 문제

# zip 사용. # zip_longest
# def solution(my_string, is_prefix):
#     for m, i in zip(my_string, is_prefix):
#         if m != i:
#             return 0
#     if len(my_string) < len(is_prefix):
#         return 0
#     return 1

# def solution(my_string, is_prefix):
#     if my_string.startswith(is_prefix):
#         return 1
#     else:
#         return 0

# 글자 이어 붙여 문자열 만들기 문제
# def solution(my_string, index_list):
#     answer = ''
#     for i in range(len(index_list)):   #index_list의 길이까지 돌린다.
#         answer += my_string[index_list[i]]
#     return answer


# 문자열의 앞의 n글자 문제
# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
# def solution(my_string, n):
#     return my_string[:n]

# 시퀀스

# 스택/큐

