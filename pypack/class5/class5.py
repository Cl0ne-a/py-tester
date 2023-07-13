from random import randint

x = 10
print(type(x))
print(bool(x))
print(not bool(x))
y = x or True
print(bool(y))
print(not bool(y))
print(x)
print(y)
a = True
b = False
print(a != b)

c = randint(2, 5)
print(c)