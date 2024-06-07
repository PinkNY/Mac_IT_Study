# 절차지향 프로그래밍

# dudgns_age = 30
# dudgns_name = "영훈"

# def introduce(name, age):
#     print(f"나는{name}이고, {age}살이야")
    
# introduce(dudgns_name, dudgns_age)


# 객체지향 프로그래밍
# 클래스, 인스턴스, 필드, 메서드, 생성자
# 객체를 만들수 있는 틀, 객체를 만들수 있는 틀(클래스)로 찍어낸 객체, 객체가 가지고 있는 성질(변수), 객체가 할수 있는 행동(함수), 


# class Human:                                # 객체를 만들 수 있는 틀
#     def __init__(self, age, name):          # 필드 : 객체가 가지고 있는 성질
#         self.age=age
#         self.name=name
        
#     # name = "dudgns"                 # 필드 : 객체가 가지고 있는 성질
#     # age = 30                        # 필드 : 객체가 가지고 있는 성질
            
#     # 메서드 (행동, 해위)
#     def introduce(self):
#         print(f"나는 {self.name}이고, {self.age}살이야")
        
# dudgns = Human(age=30, name="영훈")
# dudgns.introduce()
        
# class Human:
#     def __init__(self, name, age, location, hobby):
#         self.name=name
#         self.age=age
#         self.location=location
#         self.hobby=hobby
        
#     def introduce(self):
#         print(f"나는 {self.name}이고, {self.age}살이야.")

#     def eat(self):
#         print(f"{self.name}은 밥을 먹는다.")
        
#     def exerices(self):
#         print(f"{self.name}은 운동을 한다.")

#     def hobby(self):
#         print(f"{self.name}은 {self.hobby}을(를) 한다.")
        
# class Programmer(Human):
#     def coding(self):
#         print(f"개발자{self.name}은 코딩을 한다.")
        
# dudgns = Programmer(age=30, name="영훈", location="광주", hobby="코딩")
# dudgns.do_hobby()   


class Animal :
    legs = 0
    def walk(self):
        return ""

class Dog(Animal):
    legs = 4
    def walk(self):
        return "살랑살랑"

class Human(Animal):
    legs = 2
    def walk(self):
        return "뚜벅뚜벅"

maltese = Dog()
gildong = Human()

print(maltese.legs)
print(maltese.walk())

print(gildong.legs)
print(gildong.walk())


