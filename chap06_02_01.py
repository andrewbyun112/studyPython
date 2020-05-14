number = int(input("정수입력 > "))
try:
    if number > 0:
        raise NotImplementedError("0보다 큼")
    else:
        raise NotImplementedError("0보다 작음")
except NotImplementedError as ex:
    print("구현")
    print(ex)
    pass
except ValueError as ex:
    print("정수를 넣으세요 무조건")
except Exception as ex:
    print(type(ex))
    print(ex)
finally:
    print("무조건 실행")
    pass