print('Hello World')

# ctr+shift+P = 검색창
# -> reroad
# terminal -> ls = 디렉토리 확인
# terminal -> cd __ = 디렉토리 이동

# 함수를 사용한다 = 함수를 호출한다.
# 함수를 호출할때 여러 자료를 넣는다 그때 그 자료를 매개변수 라고 한다.
# 함수를 호출해서 최종적으로 나오는 결과를 리턴값 이라 한다.

# Shift + Alt + Up/Down(keyboard button) = 줄 복제.

print(len("Hello"))

# def 함수 이름():
#     문장

def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    
print_3_times()

# def 함수이름(매개변수, 매개변수, ...):
#     문장

def print_n_times(value, n):
    for i in range(n):
        print(value)
        
print_n_times("안녕하세요", 5)

# TypeError

def print_n_times(value, n):    # 매개변수를 2개 지정
    for i in range(n):          # range: 0~n개까지. # i를 사용하진 않아서 _로 치환해서 사용하기도 함.
        print(value)
        
print_n_times("안녕하세요")      # 하나만 넣었다.

# TypeError: print_n_times() missing 1 required positional argument: 'n'
# 'n' 하나가 빠졌다고 에러 발생

def print_n_times(value, n):            # 매개변수를 2개 지정
    for i in range(n):
        print(value)
        
print_n_times("안녕하세요", 10, 20)      # 3개를 넣었다.

#TypeError: print_n_times() takes 2 positional arguments but 3 were given
# 2개를 넣어야 하는데 3개를 넣었다고 에러 발생.

# def 함수 이름(매개변수, 매개변수, ..., 가변 매개변수):
#     문장

# 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
# 가변 매개변수는 하나만 사용 가능.

def print_n_times(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용.
        for value in values:
            print(value)
            
            print(type(values))
            # 자료형 확인.
        print()
        # 단순한 줄바꿈.
        
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
# 함수를 호출.

# 기본 매개변수 : 매개변수 = 값 형태
# 기본 매개변수는 일반 매개변수가 올 수 없다.

def print_n_times(value, n=2):
    # n번 반복한다.
    for i in range(n):
        print(value)
        
print_n_times("안녕하세요")
# 함수를 호출.

# 키워드 매개변수

def print_n_times(*values, n=2):
    # n번 반복한다.
    for i in range(n):
        # values는 리스트처럼 활용.
        for value in values:
            print(value)
            
        print()
        # 단순한 줄바꿈
        
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)
