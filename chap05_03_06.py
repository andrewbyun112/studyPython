def num_gen():
    yield 1
    yield 2
    yield 3
    yield 4
    
print(list(num_gen()))

for i in num_gen():
    print(i)