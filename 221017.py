# print 함수 : 표준 출력에 지정한 값을 출력하고 개행
# print()
# 표준 출력(standard output)
# 컴퓨터 시스템의 기본적인 출력 장치
print("Hello World!")
print()
# 변수(variable) 정의
value = 10
print()
# print 함수를 이용해 변수 value를 표준 출력에 출력
print(value)
# 아래와 같이 출력하기 위해
# value = 10
# "value = 10"
# "value = value"       // wrong
# "value = " + value    // wrong
# "value = " + 10
# "value = " + str(value)
# print("value = " + value)     // wrong
print("value = " + str(value))
print()
# print("value = " + str(10))
# print("value = " + '10')
# print("value = 10")
# 변수 value에 새로운 값을 대입
value = 20
# 변수 value를 표준 출력에 출력
print("value =" + str(value))
print()
# print 함수에서 여러 값을 출력할 수 있다.
# 이때 각 값은 쉼표(,)로 구분하며,
# 각각의  값들은 빈칸(space)로 구분되어 출력된다.
print("value =", value)
print()
# "value = 20"
# 빈칸이 아닌 다른 값으로 각각의 값들을 구분하고자 할 때는 sep 인자로 구분자를 설정한다.
# 1, 2, 3
print(1, 2, 3)                                              # 1 2 3
print(1, 2, 3, sep=", ")                                    # 1, 2, 3
print(1, 2, 3, sep=",")                                     # 1,2,3
print(1920, 1080, sep="x")                                  # 1920x1080
print()
# print 함수는 지정한 값을 출력하고, 마지막에 개행 문자("\n")을 출력한다.
# 만약 이를 다른 값으로 바꾸고자 할 때는 end 인자로 설정한다.
print("value = ")                                           # "value = \n"
print(value)                                                # "10\n"
print()
# end 인자를 설정해서 마지막에 출력되는 개행 문자를 제거할 수 있다.
# 그래서 print 함수를 여러 번 사용하더라도 한 줄에 모든 값을 출력할 수 있다.
print("value = ", end="")                                   # "value = "
print(value)                                                # "10\n"
print()
print("value", end=" = ")                                   # "value" + " = "
print(value)                                                # "10\n"
print()                                                     # "\n"
# 문자열의 format 메서드를 이용해 형식화된 문자열(formatted string)을 생성하고,
# 이 문자열을 print 함수를 이용해서 출력
value = 10
pi = 3.14159265
# value = 10, pi = 3.14
print("vlaue =", value, ", pi =", pi)                       # "value = 10 , pi = 3.14159265"
print("value = ", value, ", pi = ", pi, sep="")             # "value = 10, pi = 3.14159265"
print()
# "value = 10, pi = 3.14"
# -> "value = {}, pi = {}"

# "value = {}, pi = {}".format(value, pi)                   # "value = 10, pi = 3.14159265"
# "value = {0}, pi = {1}".format(value, pi)
# "value = {1}, pi = {0}".format(pi, value)
print("value = {}, pi = {}".format(value, pi))              # "value = 10, pi = 3.14159265"

# 서식 지정자를 이용해, 형식 문자열에 들어갈 값의 형태를 설정
# 서식 지정자 f -  소수점 형태(floating point number)로 값을 설정
print("value = {}, pi = {:f}".format(value, pi))            # "value = 10, pi = 3.141593"
print("value = {0}, pi = {1:f}".format(value, pi))           # "value = 10, pi = 3.141593"
# 서식 지정자를 이용해 형식 문자열을 생성할 때, 소수점 이하 몇 째 자리까지 값을 넣을 것이니 "정확도"를 지정할 수 있다.
print("value = {}, pi = {:.3f}".format(value, pi))          # "value = 10, pi = 3.142"
# -> 위와 같이 정확도를 지정하면, 소수점 이하 넷째 자리에서 반올림해서, 셋째 자리까지 출력
print()
# 서식 지정자를 이용해, 출력할 값의 너비를 설정
print("|1234567890|")
print("|{}".format(value))
print("|{:d}|".format(value))                               # 10진수(decimal)로 설정
print("|{:o}|".format(value))                               # 8진수(octal)로 설정
print("|{:x}|".format(value))                               # 16진수(hexadecimal)로 설정
print("|{:10d}|".format(value))                             # 너비를 지정해서 출력, 숫자는 오른쪽 정렬이 기본
print("|{:<10d}|".format(value))                            # 너비를 지정해서 출력, 왼쪽 정렬
print("|{:>10d}|".format(value))                            # 너비를 지정해서 출력, 오른쪽 정렬
print("|{:^10d}|".format(value))                            # 너비를 지정해서 출력, 가운대 정렬
print("|{:010d}|".format(value))                            # 너비를 지정해서 출력, 공백을 0으로 채움
print()
# "value = 10, pi = 3.14159265"
# 문자열의 format 메서드를 이용해 형식화된 문자열(formatted string)을 생성, print 함수 이용해서 출력
print("value = {}, pi = {}".format(value, pi))              # "value = 10, pi = 3.14159265"
# f-문자열(f-string)을 이용해, 형식화된 문자열을 생성하고, print 함수 이용해서 출력
# f-string은 파이썬 3.6에서 추가된 기능
print(f"value = {value}, pi = {pi}")                        # "value = 10, pi = 3.14159265"
# f-string에서 서식 지정자와 정확도를 지정해서, 변수 pi를 소수점 이하 셋째 자리까지의 값으로 문자열을 생성
print(f"value = {value}, pi = {pi:.3f}")                    # "value = 10, pi = 3.142"