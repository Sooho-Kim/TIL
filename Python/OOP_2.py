"""
객체 지향 프로그래밍 이해하기2 글에서 사용된 파이썬 파일입니다.
다루는 내용 : 캡슐화, 상속, 다형성, 메소드
객체 지향 프로그래밍 이해하기2 url : https://sooho-kim.tistory.com/86
"""

# 캡슐화
class Student:
    def __init__(self, name, age, id_number, grade):
        self._name = name
        self._age = age
        self._id_number = id_number
        self.__grade = grade  # __는 정보에 바로 접근할 수 없도록 막음.

    @property  # property decorator : 숨겨진 변수를 반환하게 해줌
    def grade(self):
        return self.__grade


# 인스턴스 생성
Kim = Student('Kim', 24, 201701234, 4.0)

# 변수 호출
print(Kim._name)  # kim
print(Kim._age)  # 24
print(Kim._id_number)  # 201701234
#print(Kim.__grade)  # AttributeError: 'Student' object has no attribute '__grade'

# grade를 활용해서 호출하기
grade1 = Kim.grade
print(grade1)  # 4.0

# 상속
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        return f'My name is {self._name}, I am {self._age} years old.'


class Student(Person):  # 상속할 때, object 대신에 부모클래스를 적어줘야한다.
    def __init__(self, name, age, id_number, grade):
        super().__init__(name, age)  # super()를 활용해서 부모클래스의 속성을 가져올 수 있음.
        self._id_number = id_number
        self.__grade = grade


# 인스턴스 생성
Kim = Student('kim', 24, 201701234, 4.0)

# 부모클래스로부터 상속받은 함수 사용
print(Kim.introduce())  # My name is kim, I'm 24 years old.

# 다형성
class Animal:
    def __init__(self, name):
        self._name = name

    def bark(self):  # Abstract method
        raise NotImplementedError()  # "아직 구현하지 않은 부분입니다"라는 에러입니다.


class Cat(Animal):  # 상속 받음
    def bark(self):
        return "Meow!"


class Dog(Animal):  # 상속 받음
    def bark(self):
        return "Woof!"


animals = [Cat('Mong'), Cat('Kong'), Dog('Choco')]

for animal in animals:
    print(animal.bark())  # Meow! Meow! Woof!

# 메소드
class Student:

    # 클래스 변수
    tuition_per_raise = 1.0

    def __init__(self, name, age, id_number, tuition):
        self._name = name
        self._age = age
        self._id_number = id_number
        self._tuition = tuition

    # 인스턴스 메소드
    def tuition_info(self):
        """
        return information containing class's name and tuition.
        """
        return f'{self._name}\'s tuition fee : {self._tuition*Student.tuition_per_raise}'

    # 클래스 메소드
    @classmethod
    def raise_price(cls, per): #cls : Student 클래스
        """
        change the tuition_per_raise if per >= 1.
        """
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.tuition_per_raise = per
        print('tuition increased.')

    # 스태틱 메소드
    @staticmethod
    def under_age_26(inst):
        """
        return 'over 26' if inst's age > 26, else 'under 26'
        """
        if inst._age < 27:
            return 'under 26'
        return 'over 26'

# 인스턴스 생성
Kim = Student('Kim',26,201701234,100)
Lee = Student('Lee',28,201501223,200)

# 등록금 확인
print(Kim.tuition_info()) # Kim's tuition fee : 100.0
print(Lee.tuition_info()) # Lee's tuition fee : 200.0

# 가격 인상
Student.tuition_per_raise = 1.4

# 인상 후 가격 확인
print(Kim.tuition_info()) # Kim's tuition fee : 140.0
print(Lee.tuition_info()) # Lee's tuition fee : 280.0

# 가격 인상
Student.raise_price(1.6)

# 인상 후 가격 확인
print(Kim.tuition_info()) # Kim's tuition fee : 160.0
print(Lee.tuition_info()) # Lee's tuition fee : 320.0

# 스태틱 메소드 호출
print(Kim.under_age_26(Kim)) # under 26
print(Lee.under_age_26(Lee)) # over 26