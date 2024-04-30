my_set = {1, 2, 9, 6, 8}
print(my_set)
# add numbers & string
my_set.add(5)
# update using multiple values
my_set.update([10, 20, 30])
print(my_set)
# no repeat any value
my_aa = {1, 1.0, "hello world", 2, 2, 2}
print(my_aa)
# set not support indexing

# remove
my_aa.remove(1)
print(my_aa)
# discard remove karta hai
my_aa.discard(2)
print(my_aa)
# set operation
# union -set of all element in both
a = {0, 1, 2}
b = {3, 4, 5}
print(a | b)
# intersection  -set of all element common
x = {1, 2, 3, 4, 5}
y = {1, 6, 2, 9, 8, 0}
print(x & y)
# not repeat a value
n = {1, 2, 3}
n.update([2, 5, 6])
print(n)
# remove element
c = {1, 2, 3, 2}
c.remove(2)
print(c)
