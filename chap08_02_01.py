class Student:
    def __init__(self, name, Korean, Math, English, Science):
        self.name = name
        self.Korean = Korean
        self.Math = Math
        self.English = English
        self.Science = Science

    def get_sum(self):
        return self.Korean + self.Math + self.English + \
            self.Science

    def get_average(self):
        return self.get_sum() / 4

    def get_to_string(self):
        return "{}\t{}\t{}".format(\
            self.name, self.get_sum(), self.get_average())

std = Student("윤인성", 87, 98, 88, 95)
print('Student 클래스 인스턴스 여부 : ', isinstance(std,Student))
        