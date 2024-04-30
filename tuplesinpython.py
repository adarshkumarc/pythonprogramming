e_tuple = ()
print(e_tuple)
print(type(e_tuple))
f_tuple = (1, 2, 3)
print(f_tuple)
print(f_tuple[2])

# tuple nested
n_tuple = (1, 2, 3, [2, 34, 4])
print(n_tuple)
print(n_tuple[0])
print(n_tuple[3][1])
print(n_tuple[3][2])
# negative indexing
b_tuple = (1, 2, 3, 4)
print(b_tuple[-2])
x = (1, 2, 3, (3, 2, 1))

print(x[3][2])
x = (1, 2, 3) + (1, 2, 3)

print(x)
