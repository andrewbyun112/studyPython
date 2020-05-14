# try except 연습

# try:
#     radius = int(input("정수 입력 > "))

#     print("원의 반지름 : ", radius)
#     print("원의 둘레: ", 2 * 3.141592 * radius)
#     print("원의 넓이: ", 3.141592 * radius * radius)
# except Exception as e:
#     print("type()")
# else:
#     print("예외가 발생하지 않았습니다.")
# finally:
#     print("프로그램 종료")    

# lists = ["52","273","32","스파이","103"]
# outputs = []
# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#     except:
#         pass

# print("{} 내부에 있는 숫자는".format(lists))
# print("{}입니다.".format(outputs))

# try:
#     file = open("./studyPython/./data/info.txt","w")
#     file.close()
# except Exception as e:
#     print(e)

# print("# 파일 closed 확인")
# print("file.closed: ",file.closed)


# try:
#     f = open("./studyPython/./data/info.txt","r")
#     f.write("Test!!")
# except Exception as e:
#     print(e)

# f.close()

# print("# 파일 closed 확인")
# print("file.closed: ",f.closed)

# def test():
#     print("test() 1")
#     try:
#         print("try() try")
#         return
#         print("test() after return")
#     except:
#         print("test() except")
#     else:
#         print("test() else")
#     finally:
#         print("test() finally")

#     print("test() end")

# test()

