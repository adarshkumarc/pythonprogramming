a = 10
print(type(a))
b = 10.5
print(type(b))
c = 5 + 5j
print(type(c))
d = a * 2
print(type(d))
e = a + d
print(type(e))

# list mutable hoti hai esmai hum chnge ker sakte hai
fruites = ['apple', 'banana', 'orange', 'papaya']
print(fruites[3])
print(type(fruites))

# tuple unmutable hota hai
fruites.insert(0, 'cherry')
print(fruites)
month = ('jan', 'feb', 'mar')
print(month)
a = ()
print(type(a))
# month.insert(0,'nishant')
print(len(month))
print(type(month))

# string
e = "name"
print(type(e))
# take in name variable
a = """adarsh
gurjar
age : 20
"""
print(a)

# set dont print duplicate number
f = {1, 2, 3, 4, 5, 6, 78, 9}
print(f)
print(type(f))

# dictionary: key/value
g = {1: "adarsh", 2: "kartik"}
print(type(g))
print(g[2])
