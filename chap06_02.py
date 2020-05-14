lists = [52,273,32,72,100]

try:
    inputs = int(input("정수 입력 > "))
    print("{}번째 요소 : {}".format(inputs, lists[inputs]))
    예외.발생해주세요()
except ValueError as ex:
    print(ex)
    print("정수 입력")
except IndexError as ex:
    print("인덱스가 벗어났습니다. 작은 수를 넣으세요")
except Exception as ex:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(ex),ex)
