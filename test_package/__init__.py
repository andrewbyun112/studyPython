# from modules import * 로 모듈을 읽어와서 가져올 것
__all__ = ["module_a", "module_b"]

print("test_package를 읽어 들였습니다.")

from test_package import *

print(module_a.variable_a)
print(module_b.variable_b)