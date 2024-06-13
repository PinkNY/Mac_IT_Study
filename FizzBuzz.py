# 1에서 100까지 정수들을 차례대로 출력
# 3의 배수는 정수 대신 Fizz 출력
# 5의 배수는 정수 대신 Buzz 출력
# 3과 5의 공배수는 정수 대신 FuzzBuzz를 출력

for i in range(1, 101):             # 1부터 100까지
    if i % 3 == 0 and i % 5 == 0:   # 만약 정수(i)가 3과 5의 공배수일 때
        print('FizzBuzz')           # 정수(i) 대신 'FizzBuzz'를 출력
    elif i % 3 == 0:                # 만약 정수(i)가 3의 배수일 때
        print('Fizz')               # 정수(i) 대신 'Fizz'를 출력
    elif i % 5 == 0:                # 만약 정수(i)가 5의 배수일 때
        print('Buzz')               # 정수(i) 대신 'Buzz'를 출력
    else:                           # 위 모든게 거짓일 경우
        print(i)                    # 정수(i)를 출력
print()
