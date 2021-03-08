"""
객체 지향 프로그래밍 이해하기1 글에서 사용된 파이썬 파일입니다.
다루는 내용 : 객체, 속성, 행위, 클래스,
객체 지향 프로그래밍 이해하기1 url : https://sooho-kim.tistory.com/71
"""

class Person:
    def __init__(self, name, age, gender):  # 속성(attributes)
        self._name = name
        self._age = age
        self._gender = gender

    def introduce_myself(self):  # 행위(behavior)
        """
        return a sentence containing class information(name, age)
        """
        return f"My name is {self._name}. I'm {self._age} years old."

# 실행
kim = Person("Kim", "20", "Male")  # 객체 생성
print(kim.introduce_myself())  # My name is Kim. I'm 20 years old.

# 일반적인 코딩
cellphone_company_1 = 'Apple'
cellphone_detail_1 = [{'color': 'white'}, {'price': '1000'}]

cellphone_company_2 = 'samsung'
cellphone_detail_2 = [{'color': 'black'}, {'price': '1000'}]

# 리스트 구조
cellphone_company_list = ['Apple', 'samsung']
cellphone_detail_list = [{'color': 'white', 'price': '1000'}, {'color': 'black', 'price': '1000'}]

# 딕셔너리 구조
cellphone_dict = [
    {'cellphone_company': 'Apple', 'cellphone_detail': {'color': 'white', 'price': '1000'}},
    {'cellphone_company': 'samsung', 'cellphone_detail': {'color': 'black', 'price': '1000'}}
]

# 클래스 구조
class Cellphone:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f'{self._company} - {self._details}'


phone1 = Cellphone('Apple', {'color': 'white', 'price': '1000'})
phone2 = Cellphone('samsung', {'color': 'black', 'price': '1000'})

print(phone1)  # Apple - {'color': 'white', 'price': '1000'}
print(phone2)  # samsung - {'color': 'black', 'price': '1000'}
