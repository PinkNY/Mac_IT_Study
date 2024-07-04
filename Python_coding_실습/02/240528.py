# # with 구문 이용하여 파일을 불러와서 읽기,쓰기 등이 가능.

# with open('Day2/basic.txt', 'r') as file:
#     contents = file.read()
    
# print(contents)

# #####################################

# # 람다함수를 이용하여 일회용으로 정의를 내려 사용.

# output_b = filter(lambda x: x < 300, list_input_a)
# print(list(output_b))

# output_a = map(lambda item: item * item, list_input_a)

# #######################################

# # 리스트 컨프리헨션

# print([x * x for x in list_input_a])
# print([x * x for x in list_input_a if x < 300])

# ########################################

# # map(함수, 리스트)

# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# list_input_a = [1,2,3,4,5]

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행 결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# output_b = filter(under_3, list_input_a)

# print(list(output_b))

# #############################################

# # 콜백 함수 : 함수의 매개변수에 사용하는 함수

# # 매개변수로 받은 함수를 10번 호출
# def call_10_times(func):
#     for i in range(10):
#         func()
        
# # 간단한 출력하는 함수
# def print_hello():
#     print("안녕하세요")
    
# # 조합하기    
# call_10_times(print_hello)

# ###########################################

# # 튜플과 함수

# def return_all(a,b,c):
#     return a, b, c

# print(return_all(10,20,30))
# print(type(return_all(10,20,30)))

# def return_all(*values):
#     print(f'vales의 타입은 {type(values)}')
#     return values

# print(return_all(10,20,30))
# print(type(return_all(10,20,30)))

# ############################################

# # import random

# # print(random.randrange(1,46))
# # print(random.randrange(1,46))
# # print(random.randrange(1,46))

# import user.cal as cal

# print(cal.plus(3,4))

# # user 패키지에서 cal모듈을 불러 사용하겠다.

# ##################################################

# # 객체지향 프로그래밍
# # 클래스, 인스턴스, 필드, 메서드, 생성자
# # 객체를 만들수 있는 틀, 객체를 만들수 있는 틀(클래스)로 찍어낸 객체, 객체가 가지고 있는 성질(변수), 객체가 할수 있는 행동(함수), 

# # 클래스 생성 : "클래스 클래스이름" 형식.
# # 필드 생성 : 객체가 가지는 성질을 추가.
# # __init__ 들을 이용하여 정의(def) 한다.
# # 첫 인자는 self(자신)이 들어가야 한다.
# # ex) def __init__(self, age, name):
# #         self.age=age
# #         self.name=name
# # 메서드(행동)을 지정한다.
# # ex) def introduce(self):
# #         print(f"나는 {self.name}이고, {self.age}살이야")

# # 절차지향 프로그래밍

# # dudgns_age = 30
# # dudgns_name = "영훈"

# # def introduce(name, age):
# #     print(f"나는{name}이고, {age}살이야")
    
# # introduce(dudgns_name, dudgns_age)

# # 절차지향 프로그래밍은 정의를 하고 순서대로 진행.


# class BankAccount:
#     # BankAccount 클래스를 생성.
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient funds"
#         self.balance -= amount
#         return self.balance
    
#     def __str__(self):
#         return f"BankAccount({self.owner}, Balance: {self.balance})"

# class SavingsAccount(BankAccount):
# # SavingsAccount 클래스는 BankAccount 클래스를 상속받는다.
#     def add_interest(self, interest):
#     # 이자율(interest)를 인자로 받아서 잔고에 추가.
#         self.balance += self.balance * interest
#         return self.balance
    
# class CheckingAccount(BankAccount):
#     def __init__(self, owner, balance=0, overdraft_limit=0):
#         super().__init__(owner, balance)
#         # super() = super class 부모클래스의 임시적인 객체를 반환하여 사용가능 하게.
#         # 부모 클래스의 __init__() 매직 메소드를 자식 클래스의 __init__() 매직 메소드에서 실행
#         self.overdraft_limit = overdraft_limit
#         # overdraft_limit = 최소 잔고.
        
#     def withdraw(self, money):
#           if money > self.balance + self.overdraft_limit:
#               return "Insufficient funds, overdraft limit reached"
#           self.balance -= money
#           return self.balance
#       # 금액을 인자로 받아 계좌 잔고에서 차감. 잔고와 오버드래프트 한도를 초과 시
#       # 메세지를 반환.
      
# class BankAccount:
#     transaction_log = []

#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         BankAccount.log_transaction(f"Deposit: {amount}, New balance: {self.balance}")
#         return self.balance
#     # 금액을 인자로 받아 계좌 잔고에 추가하고 그 내용을 log_transcation에 추가한다.
#     # 추가되는 금액, 추가된 새로운 잔고.

#     def withdraw(self, amount):
#         if amount > self.balance:
#             BankAccount.log_transaction(f"Withdrawal failed: {amount}, Insufficient funds")
#             return "Insufficient funds"
#         self.balance -= amount
#         BankAccount.log_transaction(f"Withdrawal: {amount}, New balance: {self.balance}")
#         return self.balance
#     # 금액을 인자로 받아 계좌 잔고에서 차감. 그 내용을 log_transcation에 추가한다.
#     # 잔고 부족일시 메세지 발생. 차감 금액, 남은 금액.

#     @classmethod
#     # 정적메소드.. 클래스에서 직접 접근할 수 있는 메소드.
#     # 인스턴스에서도 접근이 가능하다.
#     def log_transaction(cls, message):
#         # 인스턴스 메소드는 첫번째 인자로 객체 자신 self를 입력해야 한다. cls 붙은 이유.
#         cls.transaction_log.append(message)

#     @staticmethod
#     # 정적메소드.. classmethod와 비슷하지만 특별히 추가되는 인자가 없다.
#     def get_logs():
#         return BankAccount.transaction_log

#     def __str__(self):
#         return f"BankAccount({self.owner}, Balance: {self.balance})"
#     # 계좌 소유자와 잔고를 문자열로 반환.
    
# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = []
#     # 고객 클래스를 정의하여 여러 계좌를 관리할 수 있도록.

#     def add_account(self, account):
#         self.accounts.append(account)

#     def get_total_balance(self):
#         return sum(account.balance for account in self.accounts)
#     # 고객 클래스에서 계좌를 추가하고 조회할 수 있는 기능들을 구현.

#     def __str__(self):
#         return f"Customer({self.name}, Accounts: {len(self.accounts)}, Total Balance: {self.get_total_balance()})"

# class BankAccount:
#     transaction_log = []

#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         BankAccount.log_transaction(f"Deposit: {amount}, New balance: {self.balance}")
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             BankAccount.log_transaction(f"Withdrawal failed: {amount}, Insufficient funds")
#             return "Insufficient funds"
#         self.balance -= amount
#         BankAccount.log_transaction(f"Withdrawal: {amount}, New balance: {self.balance}")
#         return self.balance

#     @classmethod
#     def log_transaction(cls, message):
#         cls.transaction_log.append(message)

#     @staticmethod
#     def get_logs():
#         return BankAccount.transaction_log

#     def __add__(self, other):
#         if isinstance(other, BankAccount):
#             return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)
#         return NotImplemented

#     def __eq__(self, other):
#         if isinstance(other, BankAccount):
#             return self.balance == other.balance
#         return NotImplemented

#     def __str__(self):
#         return f"BankAccount({self.owner}, Balance: {self.balance})"
