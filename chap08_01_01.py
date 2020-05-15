def create_student(name, Korean, Math, English, Science):
    return {
        "name" : name,
        "Korean" : Korean,
        "Math" : Math,
        "English" : English,
        "Science" : Science
    }

def student_get_sum(student):
    return student["Korean"] + student["Math"] + \
        student["English"] + student["Science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student),
    ) 

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92),
]

print("이름","총점","평균",sep="\t")
for student in students:
    # print("이름:{}, 한국어:{}".format(item.get("name"),item.get("Korean")))
    # score_sum = student["Korean"] + student["Math"] + \
    #     student["English"] + student["Science"]
    # score_average = score_sum / 4

    # print(student["name"],score_sum, score_average, sep="\t") 
    print(student_to_string(student))