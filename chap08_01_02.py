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

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name, self.get_sum(), self.get_average())
# Student = Student()

Students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

#print(Students[1].name)
print("이름","총점","평균", sep="\t")
for Student in Students:
    print(str(Student))

print("마지막까지 실행 완료")