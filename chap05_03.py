# a,b=10,20
# print("swap 전")
# print("a:",a)
# print("b:",b)
# print()

# a,b = b,a
# print("swap 후")
# print("a:",a)
# print("b:",b)
# print()

# def test_func():
#     return(10,20)

# c,d = test_func()
# print("c:",c,"d:",d)

# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("Hello World")

# call_10_times(print_hello)

# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# power=  lambda x:x * x
# under_3 = lambda x:x < 3

# list_input_a = [1,2,3,4,5]

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")
# print("filter(under_3, output_b):",output_b)
# print("filter(under_3, output_b):",list(output_b))

file = open("test.txt", "w")
file.write("Hello Python Programming...!")

file.close()
