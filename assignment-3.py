
tup = (1, 2, 3, 4, 5)

y = list(tup)

y.insert(0, "Hello")
y.insert(3, "World")
y.insert(7, "Hello World")

tup = tuple(y)
print(tup)