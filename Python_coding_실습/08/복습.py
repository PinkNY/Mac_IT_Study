data = [64, 34, 25, 12, 22, 11, 90]

# 기본 정렬 (오름차순)
sorted_data = sorted(data)
print("오름차순 정렬:", sorted_data)

# 내림차순 정렬
sorted_data_desc = sorted(data, reverse=True)
print("내림차순 정렬:", sorted_data_desc)

# 키를 사용한 정렬 (길이를 기준으로 정렬)
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len) # key= lambda x: len(x) 와 같다.
print("길이 기준 정렬:", sorted_words)
