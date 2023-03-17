"""
* [property]
* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을때
* 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class Robot:

    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid range to age")
        self.__age = new_age

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.__name}. {self.__age}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


droid = Robot("R2-D2", 2)
print(droid.age)
droid.age = 11
print(droid.age)
print(droid.name)

