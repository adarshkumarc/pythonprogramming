# no name in function using lamda
multi = lambda x: x * 2
print(multi(10))
"""def multi(x):
    print(x*2)
multi(2)"""
add = lambda x, y: x + y
print(add(2, 55))
oddeven = lambda num: True if num % 2 == 0 else False
print(oddeven(55))
x = lambda x: x * 0

print(x(-1))
