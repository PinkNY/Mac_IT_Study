# 기본 은행 계좌 클래스
# class BankAccount:
# 		pass

# # 저축 계좌 클래스 (이자 기능 추가)
# class SavingsAccount(BankAccount):
# 		pass
		
# # 당좌 계좌 클래스 (오버드래프트 기능 추가)
# class CheckingAccount(BankAccount):
#     pass

# # 예시 실행
# acc = BankAccount("Charlie", 500)
# print(acc)
# print(acc.deposit(100))
# print(acc.withdraw(200))
# print(acc.withdraw(500))

# acc1 = SavingsAccount("Alice", 1000)
# acc1.add_interest(0.05)
# print(acc1)

# acc2 = CheckingAccount("Bob", 500, 200)
# print(acc2.withdraw(600))
# print(acc2)

### **문제 1: 기본 은행 계좌 클래스 구현하기**

# 1. **`BankAccount`** 클래스를 구현하세요.
#     - **`__init__`** 메소드: **`owner`**와 **`balance`**를 인자로 받아 초기화합니다.
#     - **`deposit`** 메소드: 금액을 인자로 받아 계좌 잔고에 추가합니다.
#     - **`withdraw`** 메소드: 금액을 인자로 받아 계좌 잔고에서 차감합니다. 잔고가 부족하면 "Insufficient funds" 메시지를 반환합니다.
#     - **`__str__`** 메소드: 계좌 소유자와 잔고를 문자열로 반환합니다.


### **문제 2: 저축 계좌 클래스 구현하기**

# 1. **`SavingsAccount`** 클래스를 구현하세요.
#     - **`BankAccount`** 클래스를 상속받습니다.
#     - **`add_interest`** 메소드: 이자율을 인자로 받아 잔고에 이자를 추가합니다.
    
    
    
### **문제 3: 당좌 계좌 클래스 구현하기**

# 1. **`CheckingAccount`** 클래스를 구현하세요.
#     - **`BankAccount`** 클래스를 상속받습니다.
#     - **`__init__`** 메소드: **`owner`**, **`balance`**, **`overdraft_limit`**을 인자로 받아 초기화합니다.
#     - **`withdraw`** 메소드: 금액을 인자로 받아 계좌 잔고에서 차감합니다. 잔고와 오버드래프트 한도를 초과하면
#     "Insufficient funds, overdraft limit reached" 메시지를 반환합니다.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def __str__(self):
        return f"BankAccount({self.owner}, Balance: {self.balance})"
        
     

# 테스트 코드
acc = BankAccount("Charlie", 500)
print(acc)
print(acc.deposit(100))
print(acc.withdraw(200))
print(acc.withdraw(500))

class SavingsAccount(BankAccount):
# SavingsAccount 클래스는 BankAccount 클래스를 상속받는다.
    def add_interest(self, interest):
    # 이자율(interest)를 인자로 받아서 잔고에 추가.
        self.balance += self.balance * interest
        return self.balance

# 테스트 코드
# savings = SavingsAccount("Dana", 1000)
# print(savings)
# print(savings.add_interest(0.05))
# print(savings)

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=0):
        super().__init__(owner, balance)
        # super() = super class 부모클래스의 임시적인 객체를 반환하여 사용가능 하게.
        # 부모 클래스의 __init__() 매직 메소드를 자식 클래스의 __init__() 매직 메소드에서 실행
        self.overdraft_limit = overdraft_limit
        # overdraft_limit = 최소 잔고.
        
    def withdraw(self, money):
          if money > self.balance + self.overdraft_limit:
              return "Insufficient funds, overdraft limit reached"
          self.balance -= money
          return self.balance
      # 금액을 인자로 받아 계좌 잔고에서 차감. 잔고와 오버드래프트 한도를 초과 시
      # 메세지를 반환.
    
# 테스트 코드
# checking = CheckingAccount("Eve", 500, 200)
# print(checking)
# print(checking.withdraw(600))
# print(checking.withdraw(150))
# print(checking)


class BankAccount:
    transaction_log = []

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        BankAccount.log_transaction(f"Deposit: {amount}, New balance: {self.balance}")
        return self.balance
    # 금액을 인자로 받아 계좌 잔고에 추가하고 그 내용을 log_transcation에 추가한다.
    # 추가되는 금액, 추가된 새로운 잔고.

    def withdraw(self, amount):
        if amount > self.balance:
            BankAccount.log_transaction(f"Withdrawal failed: {amount}, Insufficient funds")
            return "Insufficient funds"
        self.balance -= amount
        BankAccount.log_transaction(f"Withdrawal: {amount}, New balance: {self.balance}")
        return self.balance
    # 금액을 인자로 받아 계좌 잔고에서 차감. 그 내용을 log_transcation에 추가한다.
    # 잔고 부족일시 메세지 발생. 차감 금액, 남은 금액.

    @classmethod
    # 정적메소드.. 클래스에서 직접 접근할 수 있는 메소드.
    # 인스턴스에서도 접근이 가능하다.
    def log_transaction(cls, message):
        # 인스턴스 메소드는 첫번째 인자로 객체 자신 self를 입력해야 한다. cls 붙은 이유.
        cls.transaction_log.append(message)

    @staticmethod
    # 정적메소드.. classmethod와 비슷하지만 특별히 추가되는 인자가 없다.
    def get_logs():
        return BankAccount.transaction_log

    def __str__(self):
        return f"BankAccount({self.owner}, Balance: {self.balance})"
    # 계좌 소유자와 잔고를 문자열로 반환.

# 테스트 코드
# acc = BankAccount("Charlie", 500)
# acc.deposit(100)
# acc.withdraw(200)
# acc.withdraw(500)
# print(BankAccount.get_logs())


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    # 고객 클래스를 정의하여 여러 계좌를 관리할 수 있도록.

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)
    # 고객 클래스에서 계좌를 추가하고 조회할 수 있는 기능들을 구현.

    def __str__(self):
        return f"Customer({self.name}, Accounts: {len(self.accounts)}, Total Balance: {self.get_total_balance()})"

# 테스트 코드
# customer = Customer("Alice")
# acc1 = SavingsAccount("Alice", 1000)
# acc2 = CheckingAccount("Alice", 500, 200)
# customer.add_account(acc1)
# customer.add_account(acc2)
# print(customer)
# print(customer.get_total_balance())


class BankAccount:
    transaction_log = []

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        BankAccount.log_transaction(f"Deposit: {amount}, New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            BankAccount.log_transaction(f"Withdrawal failed: {amount}, Insufficient funds")
            return "Insufficient funds"
        self.balance -= amount
        BankAccount.log_transaction(f"Withdrawal: {amount}, New balance: {self.balance}")
        return self.balance

    @classmethod
    def log_transaction(cls, message):
        cls.transaction_log.append(message)

    @staticmethod
    def get_logs():
        return BankAccount.transaction_log

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return NotImplemented

    def __str__(self):
        return f"BankAccount({self.owner}, Balance: {self.balance})"

# 테스트 코드
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 1500)
acc3 = acc1 + acc2
print(acc3)
print(acc1 == acc2)
acc4 = BankAccount("Charlie", 1000)
print(acc1 == acc4)
