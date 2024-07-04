# 호출, 매개변수, 리턴값, 가변 매개변수, 기본 매개변수

#%%
def add(a,b):
    return a + b

add(4,3)
# %%

def add(a,b):
    c = a + b
    return None

print(add(4,3))

#%%

def add(*values):
    result = 0
    for value in values:
        resut += value
        # result = result + value
    return result

print(add(4,3,10,7))
print(add(4,3,10,7,13))

#%%

def add_multifly(*values, m=1):
    result = 0
    for value in values:
        resut += value
        # result = result + value
    return result * m

print(add_multifly(4,3,10,7, m=2))
print(add_multifly(4,3,10,7,13))


#%%

def add_multifly(*values, **kwargs):
    result = 0
    for value in values:
        resut += value
    print(kwargs)
    return result

print(add_multifly(4,3,10,7, a=10, b=20, c=30))
print(add_multifly(4,3,10,7,13))

# 가변매개변수 = *
# 키워드매개변수 = **