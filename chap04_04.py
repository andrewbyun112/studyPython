# temp = reversed([1,2,3,4,5,6])
# for i in temp:
#     print("첫 번째 반복문: {}".format(i))

# for i in temp:
#     print("두 번째 반복문: {}".format(i)


# numbers = ([1,2,3,4,5,6])
# for i in reversed(numbers):
#     print("첫 번째 반복문: {}".format(i))

# for i in reversed(numbers):
#     print("두 번째 반복문: {}".format(i))

# array = []
# for i in range(0,20,2):
#     array.append(i*i)
# print(array)

array = ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)