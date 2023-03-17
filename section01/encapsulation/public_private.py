"""
* public vs private
"""


class Robot:

    """
    Robot Class
    """

    population = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}. {self.__age}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age = age


ss = Robot("yss", 8)
ssss = Siri("iphone", 9)

